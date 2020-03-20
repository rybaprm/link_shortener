from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets

from .serializers import UserSerializer
from .models import User

class ProfileView(TemplateView):
	template_name = "users/profile.html"

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.filter(is_staff=False)
	serializer_class = UserSerializer

# Create your views here.
