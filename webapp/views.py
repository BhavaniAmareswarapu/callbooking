from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import responses
from rest_framework import status
from .models import advisor
from .serializers import advseri
class advilist(APIView):
    def get(self,request):
        ad1=advisor.objects.all()
        seri=advseri(ad1,many=True)
        return responses(seri.data)
    def post(self):
        pass