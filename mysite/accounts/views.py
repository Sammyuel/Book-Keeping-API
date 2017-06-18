from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model

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
        
        default_items = [qs_count, 23, 12, 32,12,2]
        labels = labelsNum(len(default_items))
        data = {
            "default": default_items,
  
            "labels": labels,

            }
        return JsonResponse(data)
