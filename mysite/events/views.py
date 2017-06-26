from django.shortcuts import render,redirect, get_object_or_404
from home.models import Titles
from .models import Posts, odds
from django.views.generic import View
from django.db.models import Q
from .forms import PostForm, oddsForm, eventsForm


def create_post(request, titles_Title):
    titles = get_object_or_404(Titles, Title = titles_Title, user=request.user)
    form = PostForm(request.POST or None, request.FILES or None)
    form2 = oddsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit = False)
        post.titles = get_object_or_404(Titles, Title = titles.Title, user=request.user)
        post.save()
        posts = Posts.objects.filter(titles_id = titles.id)
            
        return render(request, 'events/post_details.html', {'posts':posts, 'titles':titles})
    if form2.is_valid():
            odd = form2.save(commit = False)
            odd.titles = get_object_or_404(Titles, Title = titles.Title, user=request.user)
            odd.save()
            odd = odds.objects.filter(titles_id = titles.id)
            return render(request, 'events/post_details.html', {'odds':odd, 'titles':titles})
    return render(request, 'events/Posts.html', {'form':form, 'form2': form2, 'titles':titles})

def post_details(request, titles_Title):
    titles = get_object_or_404(Titles, Title = titles_Title, user=request.user)
    posts = Posts.objects.filter(titles = titles)
    return render(request, 'events/post_details.html',{'posts':posts, 'titles':titles})

def book_details(request, titles_Title):
    titles = get_object_or_404(Titles, Title = titles_Title, user=request.user)
    book = odds.objects.filter(titles = titles)
    return render(request, 'events/book_details.html', {'book':book, 'titles':titles})

def events_form(request):
    titles = Titles.objects.filter(user=request.user)
    form = eventsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        title = form.save(commit=False)
        title.user = request.user
        title.save()
        return render(request, 'home/home.html', {'titles':titles})
    return render(request, 'events/events_template.html', {'form':form})



class AjaxTemplateMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'ajax_template_name'):
            split = self.template_name.split('.html')
            split[-1] = '_inner'
            split.append('.html')
            self.ajax_template_name = ''.join(split)
        if request.is_ajax():
            self.template_name = self.ajax_template_name
        return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)
