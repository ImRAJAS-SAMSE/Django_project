from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# Create your views here.

#Crud operationsss

class ListTodo(generics.ListAPIView):  #read
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializers

class DetailTodo(generics.RetrieveUpdateAPIView): #update
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializers

class CreateTodo(generics.CreateAPIView):     #create
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializers

class DeleteTodo(generics.DestroyAPIView):     #delete
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializers
