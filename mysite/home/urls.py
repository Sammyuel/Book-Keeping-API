from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from . import views
from home.models import Titles
from .views import ChartData
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^events/', include('events.urls', namespace = 'events')),
    url(r'^add_title/$', views.add_title, name = 'add_title'),
    url(r'^profile/$', views.ProfileView, name = 'profile'),
    url(r'^api/chart/data/$', ChartData.as_view()),
    
    
    ]
