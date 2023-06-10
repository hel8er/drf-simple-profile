from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, views, serializers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Profile

# Create your views here.

        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        user = User.objects.create_user(username=request.username)
        if user is not None:
            user.set_password(request.password)
            user.save()
            return user


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = Profile
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}


class ProfileAPI(views.APIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        profile_serializer = UserProfileSerializer(user.profile)
        return Response(profile_serializer.data)
