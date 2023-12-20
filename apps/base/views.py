from django.shortcuts import render
from apps.base import models
from apps.secondary.models import Slide,Projects
 
# Create your views here.

def index(request):
    settings = models.Settings.objects.latest('id')
    slide = Slide.objects.latest('id')
    projects = Projects.objects.all()
    about = models.About.objects.latest('id')
    return render(request, 'base/index.html', locals())
 