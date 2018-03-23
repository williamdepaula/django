from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer


# Create your views here.

class TodoList(generics.ListCreateAPIView):

	queryset = Todo.objects.all()
	serializer_class = TodoSerializer

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer

def home(request):
	template = loader.get_template('core/index.html')
	context = {}
	return HttpResponse(template.render(context, request))
