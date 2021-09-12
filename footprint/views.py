from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from .models import Post
from .forms import PostForm

def home(request):
    return render(request, 'footprint/home.html', {'homePage': True, 'aboutPage': False, 'contactPage': False})

class PostDetailView(DetailView):
    model = Post
    hi = 3

class PostCreateView(CreateView):
    model = Post
    fields = ['peopleAmount', 'electricityUsed', 'electricityGreen', 'gasUsed', 'heatingGasUsed', 'heatingOilUsed', 'coalUsed',
    'woodUsed', 'bottledGasUsed', 'carsAmount', 'carOneSize', 'carOneMileage', 'carTwoSize', 'carTwoMileage', 'carThreeSize',
    'carThreeMileage', 'carFourSize', 'carFourMileage', 'organicFoodAmount', 'meatDairyAmount', 'localFoodAmount',
    'packagedFoodAmount', 'compostFoodAmount', 'foodWasteAmount', 'mileageEachWeekBus', 'mileageEachWeekTrain', 'hoursSpentFlying',
    'miscSpending', 'recyclePGM', 'recyclePlastic']
    template_name = 'footprint/home.html'

def about(request):
    return render(request, 'footprint/about.html', {'title': 'შესახებ', 'homePage': False, 'aboutPage': True, 'contactPage': False})

def contact(request):
    return render(request, 'footprint/contact.html', {'title': 'კონტაქტი', 'homePage': False, 'aboutPage': False, 'contactPage': True})
