from django.shortcuts import render
from apps.base import models
from apps.secondary.models import Slide,Projects
from apps.contacts.models import Contacts
# Create your views here.

def index(request):
    settings = models.Settings.objects.latest('id')
    slide = Slide.objects.latest('id')
    projects = Projects.objects.all()
    about = models.About.objects.latest('id')

    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        contacts = Contacts.objects.create(name=name, email=email, number=number)



    return render(request, 'base/index.html', locals())
 