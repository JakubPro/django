from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tweet
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomUserCreationForm

@login_required
def homeSite(request):
    tweets = Tweet.objects.all().order_by('-timestamp')
    return render(request, 'tweets/homeSite.html', {'tweets': tweets})

@login_required
def post(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Tweet.objects.create(user=request.user, content=content)
        return redirect('homeSite')
    return render(request, 'tweets/post.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST) 
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homeSite')
    else:
        form = CustomUserCreationForm()
    return render(request, 'tweets/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homeSite')
    else:
        form = AuthenticationForm()
    return render(request, 'tweets/login.html', {'form': form})
