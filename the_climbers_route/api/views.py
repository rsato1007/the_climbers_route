from django.shortcuts import render
from rest_framework import generics, status
from .serializers import RouteSerializers, CreateRouteSerializer, CreateUserSerializer, UserSerializer
from .models import Route, User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# ROUTE VIEWS
# This is a view that's set up to return to us, all the routes that have been set up.
class RouteView(generics.ListAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializers

class CreateRouteView(APIView):
    serializer_class = CreateRouteSerializer
    # This is a function called when a POST request is made.
    def post(self, request, format=None):
        
        serializer = self.serializer_class(data=request.data)
        print(serializer)
        # is.valid() ensures the data entered is the correct data before it sends it to the data base.
        # The current issue we're facing is that the data entered isn't valid.
        if serializer.is_valid():
            name = serializer.data.get('name')
            location = serializer.data.get('location')
            difficulty = serializer.data.get('difficulty')
            description = serializer.data.get('description')
            image = serializer.data.get('image')
            climb_type = serializer.data.get('climb_type')
            pitch = serializer.data.get('pitch')

            route = Route(name=name, location=location, difficulty=difficulty, description=description, image=image, climb_type=climb_type, pitch=pitch)
            route.save()

            return Response(RouteSerializers(route).data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

# USER VIEWS
class CreateUserView(APIView):
    serializer_class = CreateUserSerializer
    # This is a function called when a POST request is made.
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        print(serializer)
        # is.valid() ensures the data entered is the correct data before it sends it to the data base.
        # The current issue we're facing is that the data entered isn't valid.
        if serializer.is_valid():
            username = serializer.data.get('username')
            first_name = serializer.data.get('first_name')
            last_name = serializer.data.get('last_name')
            email = serializer.data.get('email')
            password = serializer.data.get('password')

            user = User(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            user.save()

            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)