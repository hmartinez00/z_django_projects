from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def new_view(request):
    return render(request, 'new.html')

