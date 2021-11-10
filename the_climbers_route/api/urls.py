from django.urls import path, include
from .views import RouteView, CreateRouteView, CreateUserView

urlpatterns = [
    path('route/', RouteView.as_view()),
    path('route/new', CreateRouteView.as_view()),
    path('registration/signup', CreateUserView.as_view())
]
