from django.shortcuts import render, redirect
from home.models import Post
from home.forms import HomeForm
 
def index(request):
    return render(request, 'home/index.html')

def homepage(request):
    return render(request, 'home/krittika_bootstrap.html')

def photos(request):
    return render(request, 'home/photos_bootstrap.html')

def resources(request):
    return render(request, 'home/resources.html')

def resource1(request):
    return render(request, 'home/resource1.html')

def resource2(request):
    return render(request, 'home/resource2.html')

def books(request):
    return render(request, 'home/books.html')

def telescope(request):
    return render(request, 'home/telescope.html')

def announce(request):
    return render(request, 'home/announcements_bootstrap.html')

def events(request):
    return render(request, 'home/events_bootstrap.html')

def team(request):
    return render(request, 'home/team_bootstrap.html')

def new_post(request):
    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            form.save()
            return redirect('/home')
        
        else:
            form = HomeForm()
            args = {'form' : form}
            return render(request, 'home/total.html', args) 
##            
# Create your views here.

##from django.views.generic import TemplateView
##from django.shortcuts import render, redirect

##class Homeview(TemplateView):
##    template_name = 'home/total.html'
##
##    def get(self, request):
##        form = HomeForm()
##        return render(request, self.template_name, {'form': form})
##
##    def post(self, request):
##        form = HomeForm(request.POST)
##        if form.is_valid():
##            form.save()
##            text = form.cleaned_data['post']
##            form = HomeForm()
##            return redirect('home:home')
##
##        args = {'form': form, 'text': text}
##        return render(request, self.template_name, args)

