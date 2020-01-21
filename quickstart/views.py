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



class Logout(APIView):

    def post(self, request, format=None):
        queryset = MyUser.objects.all()
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)




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
    #permission_classes = (IsAuthenticated,)
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

            user_to_object = MyUser.objects.get(id=request.data['user_to'])
            user_from_object = MyUser.objects.get(id=request.data['user_from'])

            new_friend_obj.user_to = user_to_object
            new_friend_obj.user_from = user_from_object

          #  print('New user object ', new_friend_obj)
            new_friend_obj.save()
            return Response({"message": "New Friend obj created"}, status=status.HTTP_201_CREATED)
        except Exception as error:
            return Response({"message": "Error", "data": None}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class update_request(APIView) :
    def get(self, obj):
        friend_obj = Friend.objects.get(id=1)
        print("ashgb")
        serializer = FriendSerializer(data=friend_obj)
        return Response(status=status.HTTP_200_OK)

class update_profile(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MyUserSerializer

    def get_queryset(self):
        return MyUser.objects.all()






class request_detail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FriendSerializer

    def get_queryset(self):
        return Friend.objects.filter(user_to_id=9)
a



class personal_friend(APIView):
    #  permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            print('Logged in user : ', request.user)
            myUserObj = Friend.objects.filter(user_to_id=9)
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


class List(APIView):
    def get(self, obj):
        friend_obj=Friend.objects.filter(user_to_id=9)

        friend_list = [each_object.user_from.first_name for each_object in friend_obj]
        print('Friend list : ', friend_list)

        user_obj = MyUser.objects.get(id=9)

        user_serializer = MyUserSerializer(user_obj)
        serializer = FriendSerializer(friend_obj, many=True)
        return Response({"message": "All user data", "friend_data": friend_list, 'user_data': user_serializer.data}, status=status.HTTP_200_OK)













