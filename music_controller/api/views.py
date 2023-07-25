from django.shortcuts import render
from rest_framework import generics, status
from .serializers import RoomSerializer
from .models import Room

# Create your views here.
# return to us all the different rooms that we have in our database
class RoomView(generics.ListAPIView):
  queryset = Room.objects.all()
  serializer_class = RoomSerializer
