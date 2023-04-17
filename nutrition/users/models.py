from collections.abc import Iterable
from django.db import models
from enum import Enum
from django.contrib.auth.models import User


# ИСПОЛЬЗОВАТЬ: класс-примесь для перечислителей
class EnumItems:
    @classmethod
    def items(cls: Iterable):
        return [(item.name, item.value) for item in cls]


class Sex(EnumItems, Enum):
    MALE = 'Мужской'
    FEMALE = 'Женский'


class Purpose(EnumItems, Enum):
    LOSS = 'Похудение'
    INCREASE = 'Набор веса'
    MAINTENANCE = 'Поддержание веса'


class ActivityLevel(EnumItems, Enum):
    LOW = 'Низкий'
    MIDDLE = 'Умеренный'
    HIGH = 'Высокий'
    INTENSIVE = 'Интенсивный'


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


class UserData(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    height = models.IntegerField()
    sex = models.CharField(
        max_length=2,
        # ИСПОЛЬЗОВАТЬ: теперь интересующее вас поведение перечислителей определяется не дублирующимся кодом в определении модели, а одним методом, который намного проще модифицировать при необходимости
        choices=Sex.items()
    )
    purpose = models.CharField(
        max_length=2,
        choices=Purpose.items()
    )
    activity_level = models.CharField(
        max_length=2,
        choices=ActivityLevel.items()
    )
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

