from django.urls import path
from .views import RouteView, CreateRouteView

urlpatterns = [
    path('route', RouteView.as_view()),
    path('create-route', CreateRouteView.as_view())
]
