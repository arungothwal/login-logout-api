from rest_framework import serializers

from .models import *


class MyUserSerializer(serializers.ModelSerializer):
  #  friend = serializers.StringRelatedField(many=True)
    class Meta:
        model = MyUser
        fields='__all__'



class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend


        fields='__all__'




