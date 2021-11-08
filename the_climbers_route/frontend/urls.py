from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    # Example of other URLs
    # path('route', index)
    path('create', index)
]