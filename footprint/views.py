from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from .models import Post
from .forms import PostForm

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['peopleAmount', 'electricityUsed', 'electricityGreen', 'gasUsed', 'heatingGasUsed', 'heatingOilUsed', 'coalUsed',
    'woodUsed', 'bottledGasUsed', 'carsAmount', 'carOneSize', 'carOneMileage', 'carTwoSize', 'carTwoMileage', 'carThreeSize',
    'carThreeMileage', 'carFourSize', 'carFourMileage', 'organicFoodAmount', 'meatDairyAmount', 'localFoodAmount',
    'packagedFoodAmount', 'compostFoodAmount', 'foodWasteAmount', 'mileageEachWeekBus', 'mileageEachWeekTrain', 'hoursSpentFlying',
    'miscSpending', 'recyclePGM', 'recyclePlastic']
    template_name = 'footprint/home.html'
