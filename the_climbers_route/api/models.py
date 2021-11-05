from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Route(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    difficulty = models.IntegerField()
    description = models.CharField(max_length=2200)
    # add where it's uploaded to
    image = models.FileField(blank=True, null=True)
    type = models.CharField(max_length=10)
    pitch = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    is_banned = models.BooleanField(default=False)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField()
    content = models.CharField(max_length=1250)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="likes")