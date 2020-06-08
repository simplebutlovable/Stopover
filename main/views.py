from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Search

def index(request):
    if request.method == 'GET':
        return render(request, 'base.html')

    if request.method == 'POST':
        search = request.POST.get('search')
        print(search)
        Search.objects.create(search=search)
        return render(request,'base.html')


