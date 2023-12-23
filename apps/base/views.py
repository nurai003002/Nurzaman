from django.shortcuts import render
from apps.base.models import Settings, About
from apps.secondary.models import Slide,Projects,Apartment,Kvartal,Place,Gallery,Main,Main2, Environment, Street, Reach
from apps.contacts.models import Contacts
# Create your views here.

def index(request):
    slide = Slide.objects.latest('id')
    settings = Settings.objects.latest('id')
    projects = Projects.objects.all()
    about = About.objects.latest('id')
    kvartal = Kvartal.objects.all()
    place = Place.objects.latest('id')
    gallery = Gallery.objects.latest('id')
    main = Main.objects.latest('id')
    main2 = Main2.objects.latest('id')
    environment = Environment.objects.latest('id')
    street = Street.objects.latest('id')
    reach = Reach.objects.latest('id')
    reach1 = Reach.objects.latest('id')
    apartment = Apartment.objects.latest('id')

    

    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        contacts = Contacts.objects.create(name=name, email=email, number=number)

    return render(request, 'base/index.html', locals())
