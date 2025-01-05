from django.urls import path
from . import views


urlpatterns = [
    path('', views.homeSite, name='homeSite'),
    path('post/', views.post, name='postSite'),
    path('signup/', views.signup, name='signupSite'),
    path('login/', views.login_view, name='loginSite'),
    path('like/<int:tweet_id>/', views.like_tweet, name='like_tweet'),
    path('tweet/<int:tweet_id>/', views.tweet_detail, name='tweetDetail'),
]