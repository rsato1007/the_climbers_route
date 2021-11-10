from rest_framework import serializers
from .models import Route, Profile, Review, Like, User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
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
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)


    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    # Our validators things
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'id']

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        return token