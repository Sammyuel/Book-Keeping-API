from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from . import views
from home.models import Titles


urlpatterns = [
    url(r'^(?P<titles_Title>[\w\-]+)$', views.create_post, name = 'create_post'),
    url(r'^(?P<titles_Title>[\w\-]+)/post_details', views.post_details, name='post_details'),
    url(r'^(?P<titles_Title>[\w\-]+)/book_details', views.book_details, name='book_details'),

    ]
