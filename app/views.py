from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Club
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from .serializers import ClubSerializer, RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
User = get_user_model()


# Create your views here.

class Home(viewsets.ModelViewSet):
    """
    Person creaation view
    """
    serializer_class = ClubSerializer
    queryset = Club.objects.all()
    permission_classes = [IsAuthenticated]

class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(data=serializer.data, status =status.HTTP_201_CREATED)