from django.db import models
from enum import Enum
from django.contrib.auth.models import User

# Create your models here.


class Sex(Enum):
    MALE = 'Мужской'
    FEMALE = 'Женский'


class Purpose(Enum):
    LOSS = 'Похудение'
    INCREASE = 'Набор веса'
    MAINTENANCE = 'Поддержание веса'


class ActivityLevel(Enum):
    LOW = 'Низкий'
    MIDDLE = 'Умеренный'
    HIGH = 'Высокий'
    INTENSIVE = 'Интенсивный'


class UserData(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    height = models.IntegerField()
    sex = models.CharField(max_length=2, choices=[(tag, tag.value) for tag in Sex])
    purpose = models.CharField(max_length=2, choices=[(tag, tag.value) for tag in Purpose])
    activity_level = models.CharField(max_length=2, choices=[(tag, tag.value) for tag in ActivityLevel])
    user = models.OneToOneField(User, models.CASCADE)
    product = models.ManyToManyField(
        Product,
        through='Reports',
    )
    activity = models.ManyToManyField(
        Activity,
        through='Reports',
    )



    def __str__(self):
        return f'{self.full_name} {self.age} {self.height} {self.sex} {self.purpose} {self.activity_level}'


class WeightChange(models.Model):
    date = models.DateField(auto_now=True)
    weight = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        default=0
    )
    bmi = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0
    )
    user_data = models.ForeignKey(UserData, models.CASCADE)

    def __str__(self):
        return f'{self.date} {self.weight} {self.bmi}'


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    calories = models.IntegerField()
    proteins = models.IntegerField()
    fats = models.IntegerField()
    carbohydrates = models.IntegerField()


    def __str__(self):
        return f'{self.product_name} {self.calories} {self.proteins} {self.fats} {self.carbohydrates}'



class Activity(models.Model):
    activity_name = models.CharField(max_length=50)
    burned_calories = models.IntegerField()
    runtime = models.IntegerField()


    def __str__(self):
        return f'{self.activity_name} {self.burned_calories} {self.runtime}'



class Reports(models.Model):
    date = models.DateField(auto_now=True)
    water = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=0
    )
    user_data = models.ForeignKey(UserData, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)
    activity = models.ForeignKey(Activity, models.CASCADE)

    def __str__(self):
        return f'{self.date} {self.water}'

