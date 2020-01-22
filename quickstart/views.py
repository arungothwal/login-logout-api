from rest_framework import generics
from rest_framework import status
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
import json
from django.core.serializers.json import DjangoJSONEncoder

from quickstart.serializers import MyUserSerializer ,FriendSerializer
from .models import *
from django.http import Http404


class CreateUser(APIView):

    def post(self, request):
        try:

            params = request.data
            print(params)
            user = MyUserSerializer(data=params)
            if user.is_valid(raise_exception=True):
                userObj = user.save()
                userObj.set_password(params['password'])
                userObj.save()
                return Response({"message": "signup  successfully."},user.data, status=status.HTTP_200_OK, content_type='application/json')
        except Exception as error:
            print(error)
            return Response(user.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR, content_type='application/json')



class UserLogin(APIView):

    def post(self, request):
        try:
            params = request.data
            user_exist = MyUser.objects.get(email=params['email'])
            user = authenticate(email=params['email'], password=params['password'])
            if user:
                print("ssssssssssssssss", user)
                serializer = MyUserSerializer(user)
                login(request, user)
                print("ssssssssssssssss", user.create_jwt())
                return Response(
                    {"message": "Logged in successfully.", "data": serializer.data, "token": user.create_jwt()}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Please enter correct credentials"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"message": "Email not registered."}, status=status.HTTP_404_NOT_FOUND)



class UserLogout(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        logout(request)
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)


class GetAllUser(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            myUserObj = MyUser.objects.all()
            serializer = MyUserSerializer(myUserObj, many=True)
            return Response({"message": "All user data", "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as error:
            return Response({"message": "Error", "data": None }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Friend_Request(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, obj):
        try:
            # myUserobj=Friend.objects.filter(Q(user_to_id=9) and Q(request_status='APPROVE'))
            myUserobj = Friend.objects.all()
            serializer = FriendSerializer(myUserobj, many=True)
            return Response({"message": "All user data", "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as error:
            return Response({"message": "Error", "data": None}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self,request):
      #  print('Request data : ', request.data)
        try:
            new_friend_obj = Friend()

            new_friend_obj.user_to = MyUser.objects.get(id=request.data['user_to'])
            new_friend_obj.user_from = MyUser.objects.get(id=request.data['user_from'])

          #  print('New user object ', new_friend_obj)
            new_friend_obj.save()
            return Response({"message": "New Friend obj created"}, status=status.HTTP_201_CREATED)
        except Exception as error:
            return Response({"message": "Error", "data": None}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#
# class update_request(APIView) :
#     def get(self, obj):
#         friend_obj = Friend.objects.get(id=1)
#         print("ashgb")
#         serializer = FriendSerializer(data=friend_obj)
#         return Response(status=status.HTTP_200_OK)

class update_profile(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MyUserSerializer

    def get_queryset(self):
        return MyUser.objects.all()

class request_detail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        print("Hello")

        try:
            return Friend.objects.get(pk=pk)
        except Friend.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = FriendSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)

        #
        serializer = FriendSerializer(snippet, data=request.data)
        if request.data['request_status'] == "APPROVE":
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
           # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"msg":"ajdbsbdah"}, status=status.HTTP_400_BAD_REQUEST)


        # print('Put data : ', request.data)
        # if request.data['request_status'] == "REJECT":
        #     snippet = self.get_object(pk)
        #     print("hagyjdgjdahjbasdjhdajkn",snippet)
        #
        #     del snippet
        #     return Response(status=status.HTTP_204_NO_CONTENT)


    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#
#
# class request_detail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = FriendSerializer
#
#     def get_object(self, request, pk):
#         print('Get Object method ..', pk)
#         friend_obj = Friend.objects.get(id=pk)
#         return friend_obj
#
#
#     def get_queryset(self):
#         return Friend.objects.filter(user_to_id=9)




class personal_friend(APIView):
    #  permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            print('Logged in user : ', request.user.id)
            myUserObj = Friend.objects.filter(request.user.id)
            print("hjbsajhj")
            serializer = FriendSerializer(myUserObj, many=True)
            return Response({"message": "All user data", "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as error:
            return Response({"message": "Error", "data": None}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class friend_list(APIView):
  #  permission_classes = (IsAuthenticated,)

    def get(self, request):

        try:
            myUserObj = MyUser.objects.all()
            serializer = FriendSerializer(myUserObj, many=True)
            print()

            return Response({"message": "All user data", "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as error:
            return Response({"message": "Error", "data": None }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class friend_update(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FriendSerializer
    def get_queryset(self):
        return MyUser.objects.all()


class Show_Friend(APIView):
    def get(self, obj):
        print("User", obj.user.id)

        friend_obj=Friend.objects.filter(Q(user_to_id=obj.user.id) and Q(request_status='APPROVE'))

        print('Friend object is : ', friend_obj)

        friend_list = [each_object.user_from.first_name for each_object in friend_obj]
        print('Friend list : ', friend_list)

        user_obj = MyUser.objects.get(id=obj.user.id)

        user_serializer = MyUserSerializer(user_obj)
        serializer = FriendSerializer(friend_obj, many=True)
        return Response({"message": "All user data", "friend_data": friend_list, 'user_data': user_serializer.data}, status=status.HTTP_200_OK)















