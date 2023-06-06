from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
   
    # output = ', '.join([d.nombre for d in departamentos])
    # return HttpResponse(output)
    
    context = {}
    return render(request, 'index.html', context)
