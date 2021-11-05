from rest_framework import serializers
from .model import Route, Profile, Review, Like
# Using as an example
# from .model import Room

# Using an example for study
# class RoomSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = RoomSerializer
#         fields = ('id', 'code', 'host', 'votes_to_skip')

class RouteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ('name', 'location', 'difficulty', 'description', 'image', 'type', 'pitch', 'user', 'created_at')

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