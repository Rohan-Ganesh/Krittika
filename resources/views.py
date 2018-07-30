from django.shortcuts import render

def resources(request):
    return render(request, 'resources/resources.html')

def resource1(request):
    return render(request, 'resources/resource1.html')

def resource2(request):
    return render(request, 'resources/resource2.html')

def books(request):
    return render(request, 'resources/books.html')
# Create your views here.
