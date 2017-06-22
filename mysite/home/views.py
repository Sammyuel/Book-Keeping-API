from django.shortcuts import render, redirect, get_object_or_404
from .models import Titles
from django.db.models import Q
from django.views.generic import View
from .forms import TitlesForm
from events.models import Posts
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model


User = get_user_model()
def index(request):
    if not request.user.is_authenticated():
        return render(request, 'account/login.html')
    if request.method == 'POST':
        form = ModelFormWithFileField(request.POST, request.FILES)
        if form.is_valid():
            title = form.save()
            title.Title_logo = request.FILES['Title_logo']
    titles = Titles.objects.filter(user=request.user)
    return render(request, 'home/home.html', {'titles':titles})


def add_title(request):
    titles = Titles.objects.filter(user=request.user)
    form = TitlesForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        title = form.save(commit=False)
        title.user = request.user
        title.save()
        return render(request, 'home/home.html', {'titles':titles})
    return render(request, 'home/add_title.html', {'form':form})


def ProfileView(request):
    user = request.user
    titles = Titles.objects.all()
    posts = Posts.objects.all()
    return render(request, 'home/profile.html', {'user':user,'titles':titles, 'posts':posts})

    
def labelsNum(number):
    x_axis = []
    for i in range(number):
        x_axis.append(i)
    return x_axis



class ChartData(APIView):

    authentication_classes = []
    permission_classes = []
    

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        posts = Posts.objects.all()
        profit = 0
        default_items = []
        profits = []
        for post in posts:
            default_items.append(post.receive_ammount - post.bet_ammount)
        for i in range(len(default_items)):
            if i == 0:
                profits.append(default_items[i])
            else:
                profits.append(default_items[i]+profits[i-1])
            
        labels = labelsNum(len(default_items))
            
        data = {
            "default": profits,
  
            "labels": labels,

            }
        all_titles = Titles.objects.all()
        for title in all_titles:
            single_items = []
            single_profits = []
            game_post = Posts.objects.filter(titles = title)
            for post in game_post:
                single_items.append(post.receive_ammount - post.bet_ammount)
            for i in range(len(single_items)):
                if i == 0:
                    profits.append(single_items[i])
                else:
                    profits.append(default_items[i]+profits[i-1])
            data[title.Title] = single_profits
        return JsonResponse(data)
