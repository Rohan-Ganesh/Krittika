from django.shortcuts import render

def event(request):
    return render(request, 'events_bootstrap.html')
# Create your views here.
