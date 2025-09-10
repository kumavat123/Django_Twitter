from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .models import Twitter
from .forms import TwitterForm ,UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request, 'index.html')

# for listing all the tweets on a page
def Twitter_List(request):
    twitters = Twitter.objects.all().order_by('-created_at')
    return render(request, 'Twitter_List.html', {'twitters':twitters})
# to create tweets
#also we need to add protection to create twitter
@login_required
def Twitter_create(request):
    if request.method == 'POST':
        form = TwitterForm(request.POST, request.FILES)
        if form.is_valid():
            twitter=form.save(commit=False)
            twitter.user=request.user
            twitter.save()
        return redirect('Twitter_List')
    else:
       form = TwitterForm(request.POST)
    return render(request, 'Twitter_form.html', {'form':form})

# to edit the course
@login_required
def Twitter_edit(request,twitter_id):
    twitter=get_object_or_404(Twitter, pk=twitter_id, user=request.user)
    if request.method == 'POST':
        form = TwitterForm(request.POST, request.FILES, instance=twitter)
        if form.is_valid():
            twitter=form.save(commit=False)
            twitter.user=request.user
            twitter.save()
        return redirect('Twitter_List')
    else:
        form = TwitterForm(instance=twitter)
    return render(request, 'Twitter_form.html', {'form':form})

# to delete the tweet
def Twitter_delete(request,twitter_id):
    twitter=get_object_or_404(Twitter, pk=twitter_id, user=request.user)
    if request.method == 'POST':
        twitter.delete()
        return redirect('Twitter_List')
    return render(request, 'Twitter_Delete.html', {'twitter':twitter})

# before this make a folder in outer template folder named as registration
def register(request):
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('Twitter_List')
            # now after this go to urls.py
    else:
        form = UserRegistrationForm(request.POST)
    return render(request, 'registration/register.html', {'form': form})