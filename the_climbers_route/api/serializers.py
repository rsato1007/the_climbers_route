from rest_framework import serializers
from .models import Route, Profile, Review, Like, User
# Using as an example
# from .model import Room

# Using an example for study
# class RoomSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = RoomSerializer
#         fields = ('id', 'code', 'host', 'votes_to_skip')


# These convert the python code into some format we can use. In this case, it will convert into JSON objects.
class RouteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ('name', 'location', 'difficulty', 'description', 'image', 'climb_type', 'pitch', 'user', 'created_at')

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'location', 'is_admin', 'is_banned')

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('user', 'route', 'rating', 'content', 'posted_at')

class LikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('user', 'review')

class CreateRouteSerializer(serializers.ModelSerializer):
    # Serialize classes that map closely to Django models.
    class Meta:
        model = Route
        fields = ['name', 'location', 'difficulty', 'description', 'image', 'climb_type', 'pitch']

# USER SERIALIZER

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'id']