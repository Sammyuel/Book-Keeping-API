from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from .views import ChartData

urlpatterns = [
    url(r'^accounts/profile/', ChartData.as_view()),
    url(r'^profile/', ChartData.as_view()),

]
if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
