from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tweet, Like
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomUserCreationForm
from django.db import models

@login_required
def homeSite(request):
    sort_order = request.GET.get('sort', 'desc')
    sort_by_likes = request.GET.get('likes', None)

    if sort_by_likes:
        tweets = Tweet.objects.annotate(like_count=models.Count('likes')).order_by('-like_count')
    elif sort_order == 'asc':
        tweets = Tweet.objects.all().order_by('timestamp')
    else:
        tweets = Tweet.objects.all().order_by('-timestamp')

    return render(request, 'tweets/homeSite.html', {'tweets': tweets, 'sort_order': sort_order})

@login_required
def post(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Tweet.objects.create(user=request.user, content=content)
        return redirect('homeSite')
    return render(request, 'tweets/postSite.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homeSite')
    else:
        form = CustomUserCreationForm()
    return render(request, 'tweets/signupSite.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homeSite')
    else:
        form = AuthenticationForm()
    return render(request, 'tweets/loginSite.html', {'form': form})

@login_required
def like_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)

    if not Like.objects.filter(user=request.user, tweet=tweet).exists():
        Like.objects.create(user=request.user, tweet=tweet)

    if request.GET.get('next') == 'home':
        return redirect('homeSite') 
    else:
        return redirect('tweetDetail', tweet_id=tweet.id)

@login_required
def tweet_detail(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)

    like_count = tweet.likes.count()

    return render(request, 'tweets/tweetDetail.html', {
        'tweet': tweet,
        'like_count': like_count,
    })