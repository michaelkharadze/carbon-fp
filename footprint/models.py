from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

class electricityChoices(models.IntegerChoices):
    Small = 3000, _('პატარა ზომის სახლი / ბინა (3000 კვტ/სთ)')
    Medium = 4800, _('საშუალო ზომის სახლი (4800 კვტ/სთ)')
    Large = 7000, _('დიდი ზომის სახლი (7000 კვტ/სთ)')
    Residence = 2000, _('დარბაზული სახლი (2000 კვტ/სთ)')

class gasChoices(models.IntegerChoices):
    Small = 12000, _('პატარა ზომის სახლი / ბინა (12000 კვტ/სთ)')
    Medium = 18000, _('საშუალო ზომის სახლი (18000 კვტ/სთ)')
    Large = 27000, _('დიდი ზომის სახლი (27000 კვტ/სთ)')
    Residence = 5000, _('დარბაზული სახლი (5000 კვტ/სთ)')

class heatingGasChoices(models.IntegerChoices):
    No = 0, _('არა')
    Yes = 1, _('დიახ')

class electricityGreenChoices(models.IntegerChoices):
    No = 100, _('არა')
    Yes = 75, _('დიახ')

class carsAmountChoices(models.IntegerChoices):
    Zero = 0, '0'
    One = 1, '1'
    Two = 2, '2'
    Three = 3, '3'
    Four = 4, '4'

class carSizeChoices(models.IntegerChoices):
    sportsCar = 35, _('სპორტული მანქანა ან დიდი ჯიპი')
    smallMediumCar = 46, _('პატარა/საშუალო ზომის ჯიპი ან მინივენი')
    estateCar = 52, _('პატარა, საშუალო ან დიდი უნივერსალი')

class carMileageChoices(models.IntegerChoices):
    lowMileage = 6000, _('დაბალი (10000 კმ)')
    mediumMileage = 9000, _('საშუალო (15000 კმ)')
    highMileage = 12000, _('მაღალი (20000 კმ)')

class organicFoodChoices(models.IntegerChoices):
    neverEat = 7, _('არასდროს')
    sometimesEat = 5, _('ხანდახან')
    mostlyEat = 2, _('უმეტესად')
    alwaysEat = 0, _('ყოველთვის')

class meatDairyChoices(models.IntegerChoices):
    moreThanAverage = 60, _('საშუალოზე მეტს')
    averageAmount = 40, _('საშუალო რაოდენობას')
    belowAverage = 25, _('საშუალოზე ნაკლებს')
    lactoVegetarian = 10, _('არ მივირთმევ ხორცს')
    vegetarian = 0, _('არ მივირთმევ არც ხორცს და არც რძეს')

class localFoodChoices(models.IntegerChoices):
    veryLittle = 5, _('ძალიან მცირე')
    averageAmount = 3, _('საშუალო')
    moreThanAverage = 2, _('საშუალოზე მეტი')
    almostall = 1, _('თითქმის მთლიანად')

class compostChoices(models.IntegerChoices):
    neverEat = 2, _('არასდროს')
    sometimesEat = 1, _('ხანდახან')
    alwaysEat = 0, _('ყოველთვის')

class packagedChoices(models.IntegerChoices):
    moreThanAverage = 60, _('დიდი რაოდენობა')
    averageAmount = 40, _('საშუალო რაოდენობა')
    belowAverage = 20, _('მცირე რაოდენობა')
    lactoVegetarian = 5, _('ძალიან მცირე')

class wastedChoices(models.IntegerChoices):
    moreThanAverage = 148, _('დიდი რაოდენობა')
    averageAmount = 125, _('საშუალო რაოდენობა')
    belowAverage = 103, _('მცირე რაოდენობა')
    lactoVegetarian = 86, _('ძალიან მცირე')

class miscSpendingChoices(models.IntegerChoices):
    moreThanAverage = 50, _('დიდი რაოდენობა')
    averageAmount = 34, _('საშუალო რაოდენობა')
    belowAverage = 24, _('მცირე რაოდენობა')
    lactoVegetarian = 14, _('ძალიან მცირე')

class recyclePGMChoices(models.IntegerChoices):
    No = 0, _('არა')
    Yes = 7, _('დიახ')

class recyclePlasticChoices(models.IntegerChoices):
    No = 0, _('არა')
    Yes = 14, _('დიახ')

class Post(models.Model):
    peopleAmount = models.IntegerField(verbose_name=_(" რამდენი ადამიანი ცხოვრობს თქვენთან სახლში? (თქვენ ჩათვლით)"))
    electricityUsed = models.IntegerField(blank=True, null=True, choices=electricityChoices.choices, verbose_name=_(" რა რაოდენობით დენი მოიხმარება თქვენ სახლში?"))
    electricityGreen = models.IntegerField(default=100, choices=electricityGreenChoices.choices, verbose_name=_(" იყენებთ მწვანე ენერგიას?"))
    gasUsed = models.IntegerField(blank=True, null=True, default=0, choices=gasChoices.choices, verbose_name=_(" რა რაოდენობით გაზი მოიხმარება თქვენ სახლში?"))
    heatingGasUsed = models.BooleanField(default=0, choices=heatingGasChoices.choices, verbose_name=_(" გამოიყენება თქვენ სახლში ზეთი, ქვანახშირი, შეშა ან ჩამოსხმული გაზი გასათბობად?"))
    heatingOilUsed = models.IntegerField(blank=True, null=True, verbose_name=_(" გამოყენებული ზეთი გასული წლის განმავლობაში (ლიტრებში)"))
    coalUsed = models.IntegerField(blank=True, null=True, verbose_name=_(" გამოიყენებული ქვანახშირი გასული წლის განმავლობაში (კილოგრამებში)"))
    woodUsed = models.IntegerField(blank=True, null=True, verbose_name=_(" გამოყენებული შეშა გასული წლის განმავლობაში (კილოგრამებში)"))
    bottledGasUsed = models.IntegerField(blank=True, null=True, verbose_name=_(" გამოყენებული ჩამოსხმული გაზი გასული წლის განმავლობაში (კილოგრამებში)"))
    carsAmount = models.IntegerField(default=0, null=True, choices=carsAmountChoices.choices, verbose_name=_(" რამდენი მანქანაა თქვენ ოჯახში?"))
    carOneSize = models.IntegerField(blank=True, null=True, default=1, choices=carSizeChoices.choices, verbose_name=_(" მანქანა 1 ზომა:"))
    carOneMileage = models.IntegerField(blank=True, null=True, default=0, choices=carMileageChoices.choices, verbose_name=_(" მანქანა 1 გარბენი:"))
    carTwoSize = models.IntegerField(blank=True, null=True, default=1, choices=carSizeChoices.choices, verbose_name=_(" მანქანა 2 ზომა:"))
    carTwoMileage = models.IntegerField(blank=True, null=True, default=0, choices=carMileageChoices.choices, verbose_name=_(" მანქანა 2 გარბენი:"))
    carThreeSize = models.IntegerField(blank=True, null=True, default=1, choices=carSizeChoices.choices, verbose_name=_(" მანქანა 3 ზომა:"))
    carThreeMileage = models.IntegerField(blank=True, null=True, default=0, choices=carMileageChoices.choices, verbose_name=_(" მანქანა 3 გარბენი:"))
    carFourSize = models.IntegerField(blank=True, null=True, default=1, choices=carSizeChoices.choices, verbose_name=_(" მანქანა 4 ზომა:"))
    carFourMileage = models.IntegerField(blank=True, null=True, default=0, choices=carMileageChoices.choices, verbose_name=_(" მანქანა 4 გარბენი:"))

    organicFoodAmount = models.DecimalField(max_digits=6, null=True, decimal_places=2, blank=True, default=7, choices=organicFoodChoices.choices, verbose_name=_(" რა რაოდენობით მიირთმევთ ორგანულ საკვებს"))
    meatDairyAmount = models.DecimalField(max_digits=6, null=True, decimal_places=2, blank=True, default=40, choices=meatDairyChoices.choices, verbose_name=_(" რა რაოდენობით მიირთმევთ ხორცს ან/და რძეს?"))
    localFoodAmount = models.DecimalField(max_digits=6, null=True, decimal_places=2, default=3, choices=localFoodChoices.choices, verbose_name=_(" თქვენი საკვების რა ნაწილია წარმოებული ადგილობრივად?"))
    packagedFoodAmount = models.DecimalField(max_digits=6, null=True, decimal_places=2, blank=True, default=0, choices=packagedChoices.choices, verbose_name=_(" თქვენი საკვების რა ნაწილია შეფუთული?"))
    compostFoodAmount = models.DecimalField(max_digits=6, null=True, decimal_places=2, default=0.2, choices=compostChoices.choices, verbose_name=_(" რამდენად უკეთებთ კომპოსტირებას ნარჩენ და გამოუყენებელ საკვებს?"))
    foodWasteAmount = models.DecimalField(max_digits=6, null=True, decimal_places=2, default=0.5, choices=wastedChoices.choices, verbose_name=_(" რა რაოდენობით საკვებს ფლანგავთ?"))
    mileageEachWeekBus = models.IntegerField(blank=True, null=True, verbose_name=_(" კვირაში რამდენ კილომეტრს მგზავრობთ ავტობუსით?"))
    mileageEachWeekTrain = models.IntegerField(blank=True, null=True, verbose_name=_(" კვირაში რამდენ კილომეტრს მგზავრობთ მატარებლით?"))
    hoursSpentFlying = models.IntegerField(blank=True, null=True, verbose_name=_(" წელიწადში რამდენ საათს ატარებთ თვითმფრინავში?"))
    miscSpending = models.DecimalField(max_digits=6, null=True, decimal_places=2, default=34, choices=miscSpendingChoices.choices, verbose_name=_(" რა რაოდენობას ხარჯავთ სხვადასხვა ხარჯებში?"))
    recyclePGM = models.DecimalField(max_digits=6, null=True, decimal_places=2, blank=True, default=0, choices=recyclePGMChoices.choices, verbose_name=_(" ქაღალდს, მინას და ლითონს ამუშავებთ?"))
    recyclePlastic = models.DecimalField(max_digits=6, null=True, decimal_places=2, blank=True, default=0, choices=recyclePlasticChoices.choices, verbose_name=_(" პლასტმასს ამუშავებთ გარდა პოლიეთილენის პარკებისა?"))
    totalAmount = 0
    planetsAmount = 0
    electricityAmount = 0
    transportationAmount = 0
    foodAmount = 0
    miscAmount = 0
    components = [0, 0, 0, 0]
    
    def __str__(self):
        num = float(self.electricityUsed or 0) * 2.16 / 7000 * float(self.electricityGreen or 0) / 100 / float(self.peopleAmount or 1) + float(self.gasUsed or 0) * 2.44 / 12000 / float(self.peopleAmount or 1)
        + float(self.heatingOilUsed or 0) * 3 / 1000 / float(self.peopleAmount or 1) + float(self.coalUsed or 0) * 3.3 / 1000 / float(self.peopleAmount or 1) + float(self.woodUsed or 0) * 0.1 / 1000 / float(self.peopleAmount or 1)
        + float(self.bottledGasUsed or 0) * 3.7 / 100 / float(self.peopleAmount or 1) + float(self.carOneMileage or 0) / float(self.carOneSize or 1) * 0.86 / 60 / float(self.peopleAmount or 1)
        + float(self.carTwoMileage or 0) / float(self.carTwoSize or 1) * 0.86 / 60 / float(self.peopleAmount or 1) + float(self.carThreeMileage or 0) / float(self.carThreeSize or 1) * 0.86 / 60 / float(self.peopleAmount or 1)
        + float(self.carFourMileage or 0) / float(self.carFourSize or 1) * 0.86 / 60 / float(self.peopleAmount or 1) + float(self.organicFoodAmount or 0) / 10 + float(self.meatDairyAmount or 0) / 100
        + float(self.localFoodAmount or 0) / 10 + float(self.packagedFoodAmount or 0) / 100 + float(self.compostFoodAmount or 0) / 10 + float(self.foodWasteAmount or 0) / 100
        + (float(self.mileageEachWeekBus or 0) * 1.6 + float(self.mileageEachWeekTrain or 0) * 1.6) * 52 / 10000 + float(self.hoursSpentFlying or 0) / 4 + float(self.miscSpending or 0) / 10
        - float(self.recyclePGM or 0) / 100 - float(self.recyclePlastic or 0) / 100
        valueToReturn = format(num, '.2f')
        return str(valueToReturn)
        

    def __init__(self,*args,**kwargs):
        super(Post, self).__init__(*args, **kwargs)
        num = float(self.electricityUsed or 0) * 2.16 / 7000 * float(self.electricityGreen or 100) / 100 / float(self.peopleAmount or 1) + float(self.gasUsed or 0) * 2.44 / 12000 / float(self.peopleAmount or 1)
        + float(self.heatingOilUsed or 0) * 3 / 1000 / float(self.peopleAmount or 1) + float(self.coalUsed or 0) * 3.3 / 1000 / float(self.peopleAmount or 1) + float(self.woodUsed or 0) * 0.1 / 1000 / float(self.peopleAmount or 1)
        + float(self.bottledGasUsed or 0) * 3.7 / 100 / float(self.peopleAmount or 1) + float(self.carOneMileage or 0) / float(self.carOneSize or 52) * 0.86 / 60 / float(self.peopleAmount or 1)
        + float(self.carTwoMileage or 0) / float(self.carTwoSize or 52) * 0.86 / 60 / float(self.peopleAmount or 1) + float(self.carThreeMileage or 0) / float(self.carThreeSize or 52) * 0.86 / 60 / float(self.peopleAmount or 1)
        + float(self.carFourMileage or 0) / float(self.carFourSize or 52) * 0.86 / 60 / float(self.peopleAmount or 1) + float(self.organicFoodAmount or 7) / 10 + float(self.meatDairyAmount or 40) / 100
        + float(self.localFoodAmount or 0) / 10 + float(self.packagedFoodAmount or 0) / 100 + float(self.compostFoodAmount or 0) / 10 + float(self.foodWasteAmount or 0) / 100
        + (float(self.mileageEachWeekBus or 0) * 1.6 + float(self.mileageEachWeekTrain or 0) * 1.6) * 52 / 10000 + float(self.hoursSpentFlying or 0) / 4 + float(self.miscSpending or 0) / 10
        - float(self.recyclePGM or 0) / 100 - float(self.recyclePlastic or 0) / 100
        valueToReturn = format(num, '.2f')
        numAlternative = num * 4.5 / 12
        planetsToReturn = format(numAlternative, '.2f')
        numTwo = float(self.electricityUsed or 0) * 2.16 / 7000 * float(self.electricityGreen or 100) / 100 / float(self.peopleAmount or 1) + float(self.gasUsed or 0) * 2.44 / 12000 / float(self.peopleAmount or 1)
        + float(self.heatingOilUsed or 0) * 3 / 1000 / float(self.peopleAmount or 1) + float(self.coalUsed or 0) * 3.3 / 1000 / float(self.peopleAmount or 1) + float(self.woodUsed or 0) * 0.1 / 1000 / float(self.peopleAmount or 1)
        + float(self.bottledGasUsed or 0) * 3.7 / 100 / float(self.peopleAmount or 1)
        electricityToReturn = format(numTwo, '.2f')
        numThree = float(self.carOneMileage or 0) / float(self.carOneSize or 52) * 0.86 / 60 / float(self.peopleAmount or 1) + float(self.carTwoMileage or 0) / float(self.carTwoSize or 52) * 0.86 / 60 / float(self.peopleAmount or 1)
        + float(self.carThreeMileage or 0) / float(self.carThreeSize or 52) * 0.86 / 60 / float(self.peopleAmount or 1) + float(self.carFourMileage or 0) / float(self.carFourSize or 52) * 0.86 / 60 / float(self.peopleAmount or 1)
        + (float(self.mileageEachWeekBus or 0) * 1.6 + float(self.mileageEachWeekTrain or 0) * 1.6) * 52 / 10000 + float(self.hoursSpentFlying or 0) / 4
        transportationToReturn = format(numThree, '.2f')
        numFour = float(self.organicFoodAmount or 7) / 10 + float(self.meatDairyAmount or 40) / 100 + float(self.localFoodAmount or 0) / 10
        + float(self.packagedFoodAmount or 0) / 100 + float(self.compostFoodAmount or 0) / 10 + float(self.foodWasteAmount or 0) / 100
        foodToReturn = format(numFour, '.2f')
        numFive = float(self.miscSpending or 0) / 10 - float(self.recyclePGM or 0) / 100 - float(self.recyclePlastic or 0) / 100
        miscToReturn = format(numFive, '.2f')
        self.totalAmount = valueToReturn
        self.planetsAmount = planetsToReturn
        self.electricityAmount = electricityToReturn
        self.transportationAmount = transportationToReturn
        self.foodAmount = foodToReturn
        self.miscAmount = miscToReturn
        self.components = [electricityToReturn, transportationToReturn, foodToReturn, miscToReturn]
        self.components.sort(reverse=True)
    
    def get_absolute_url(self):
        return reverse('footprint-detail', kwargs={'pk': self.pk})