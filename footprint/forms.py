from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'peopleAmount', 'electricityUsed', 'electricityGreen', 'gasUsed',
            'heatingGasUsed', 'heatingOilUsed', 'coalUsed', 'woodUsed',
            'bottledGasUsed', 'carsAmount', 'carOneSize', 'carOneMileage',
            'carTwoSize', 'carTwoMileage', 'carThreeSize', 'carThreeMileage',
            'carFourSize', 'carFourMileage', 'organicFoodAmount',
            'meatDairyAmount', 'localFoodAmount', 'packagedFoodAmount',
            'compostFoodAmount', 'foodWasteAmount', 'mileageEachWeekBus',
            'mileageEachWeekTrain', 'hoursSpentFlying', 'miscSpending',
            'recyclePGM', 'recyclePlastic'
        ]