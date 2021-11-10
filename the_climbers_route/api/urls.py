from django.urls import path, include
from .views import RouteView, CreateRouteView, CreateUserView, ObtainTokenPairWithView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('route/', RouteView.as_view()),
    path('route/new', CreateRouteView.as_view()),
    path('registration/signup', CreateUserView.as_view()),
    path('token/obtain/', ObtainTokenPairWithView.as_view(), name='token_create'), # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
