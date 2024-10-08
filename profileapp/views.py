from django.shortcuts import render
from .models import *
# Create your views here.

def home_view(request):
    profile = Profile.objects.get(email='nwekelesley@gmail.com')
    technologies = Technologies.objects.filter(user=profile)
    services = Services.objects.filter(user=profile)
    projects = Projects.objects.filter(user=profile)
    clients = Clients.objects.filter(seller_profile=profile)
    context={'profile':profile,
             'clients':clients,
             'technologies':technologies,
             'services':services,
             'projects':projects,}
    return render(request,'index.html', context)