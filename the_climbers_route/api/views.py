from django.shortcuts import render
from rest_framework import generics, status, viewsets, permissions
from .serializers import RouteSerializers, CreateRouteSerializer, CreateUserSerializer, UserSerializer, MyTokenObtainPairSerializer
from .models import Route, User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

# The authenticator function
JWT_authenticator = JWTAuthentication()

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
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Token Views
class ObtainTokenPairWithView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer