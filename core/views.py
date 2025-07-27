from django.shortcuts import render
from datetime import datetime

def home(request):
    return render(request, 'home.html', {'year' : datetime.now().year })

def cv(request):
    return render(request, 'cv.html', {'year' : datetime.now().year })

def reading(request):
    return render(request, 'reading.html', {'year' : datetime.now().year })
