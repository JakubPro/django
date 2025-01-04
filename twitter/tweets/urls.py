from django.urls import path
from . import views


urlpatterns = [
    path('', views.homeSite, name='homeSite'),
    path('post/', views.post, name='post'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
]