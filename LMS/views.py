from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import models

def index(request):
    return render(request,'index.html')


def customer(request):
    data= models.borrowers.objects.all()
    return render(request,'customer.html', { 'data' : data})
