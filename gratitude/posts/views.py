from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from posts.models import *
from .forms import PostForm

# Create your views here.

def list(request):
    posts = Post.objects.all()
    for post in posts:
        for user in post.recipients.all():
            print(user.profile)
    return render(request, 'posts/list.html', locals())

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('posts')
    else:
        form = PostForm()
        return render(request, 'posts/new.html', {'form': form})
