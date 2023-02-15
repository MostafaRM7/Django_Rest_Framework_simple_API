from django.contrib.auth.models import User
from rest_framework import viewsets, permissions

from .models import Course
from .serializers import CourseSerializer, UserSerializer


class CourseView(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAdminUser]
