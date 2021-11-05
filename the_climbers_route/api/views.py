from django.shortcuts import render
from rest_framework import generics
from .serializers import RouteSerializers
from .models import Route

# Create your views here.
# This is a view that's set up to return to us, all the routes that have been set up.
class RouteView(generics.CreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializers