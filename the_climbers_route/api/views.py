from django.shortcuts import render
from rest_framework import generics
from .serializers import RouteSerializers, CreateRouteSerializer
from .models import Route
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
# This is a view that's set up to return to us, all the routes that have been set up.
class RouteView(generics.ListAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializers

class CreateRouteView(APIView):
    serializer_class = CreateRouteSerializer

    def post(self, request, format=None):
        if not self.request.exists(self.request.session.session_key):
            self.request.session.create()
        
        serializer = self.serializers_class(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            location = serializer.data.get('location')
            difficulty = serializer.data.get('difficulty')
            description = serializer.data.get('description')
            image = serializer.data.get('image')
            type = serializer.data.get('type')
            pitch = serializer.data.get('pitch')
            user = self.request.session.session_key
        route = Route(name=name, location=location, difficulty=difficulty, description=description, image=image, type=type, pitch=pitch, user=user)
        route.save()

        return Response(RouteSerializers(route).data, status=status.HTTP_202)
