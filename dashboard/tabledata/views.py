from django.shortcuts import render, redirect
from .models import TableData

def tabledata(request):
    data = TableData.objects.all()
    return render(request, 'tabledata.html', {'data': data})

def add_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        value = request.POST.get('value')
        data = TableData(name=name, value=value)
        data.save()
        return redirect('tabledata')
