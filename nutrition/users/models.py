from collections.abc import Iterable
from django.db import models
from enum import Enum
from django.contrib.auth.models import User


# ИСПОЛЬЗОВАТЬ: класс-примесь для перечислителей
class EnumItems:
    @classmethod
    def items(cls: Iterable):
        # КОММЕНТАРИЙ: первый элемент кортежа должен быть собственно тем значением поля, которое будет проверяться — лучше явно указать атрибут name (строку) экземпляра перечислителя, а не сам экземпляр перечислителя
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
    # КОММЕНТАРИЙ: не лучше ли здесь использовать models.TimeField?
    runtime = models.IntegerField()

    def __str__(self):
        return f'{self.activity_name} {self.burned_calories} {self.runtime}'


class UserData(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    height = models.IntegerField()
    sex = models.CharField(
        # ИСПРАВИТЬ здесь и далее: в это поле должен быть записан первый элемент какого-то из кортежей внутри choices — а их длина больше двух символов
        max_length=6,
        # ИСПОЛЬЗОВАТЬ: теперь интересующее вас поведение перечислителей определяется не дублирующимся кодом в определении модели, а одним методом, который намного проще модифицировать при необходимости
        choices=Sex.items()
    )
    purpose = models.CharField(
        max_length=11,
        choices=Purpose.items()
    )
    activity_level = models.CharField(
        max_length=9,
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
        # КОММЕНТАРИЙ: если я правильно понимаю, то экземпляр этой модели (и запись в таблице) будет создаваться каждый раз, когда пользователь в отдельной от общего отчёта формочке введёт свой новый вес
        # УДАЛИТЬ: если так, то зачем здесь значение по умолчанию? не вижу смысла хранить в таблице нулевые значения
    )
    # КОММЕНТАРИЙ: не забудьте, что значение для этого поля должно не вводиться пользователем, а рассчитываться (в представлении или форме) на основании нового веса и роста конкретного пользователя
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

