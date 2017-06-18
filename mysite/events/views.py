from django.shortcuts import render,redirect, get_object_or_404
from home.models import Titles
from .models import Posts
from django.views.generic import View
from django.db.models import Q
from .forms import PostForm


def create_post(request, titles_Title):
    titles = get_object_or_404(Titles, Title = titles_Title, user=request.user)
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit = True)
        post.save()
        posts = Posts.objects.all()
        titles.save()
        return render(request, 'events/post_details.html', {'posts':posts, 'titles':titles})
    
    return render(request, 'events/Posts.html', {'form':form, 'titles':titles})

def post_details(request, titles_Title):
    titles = get_object_or_404(Titles, Title = titles_Title, user=request.user)
    posts = Posts.objects.all()

    return render(request, 'events/post_details.html',{'posts':posts, 'titles':titles})

