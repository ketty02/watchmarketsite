from django.db import models
from django.core.validators import MinValueValidator
from market.models.category import Subcategory
from market.models.watch import Watch

class Type(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    watch = models.ManyToManyField(Watch, through='WatchType', related_name='watches')
    name = models.CharField(unique=True, max_length=255)
    case_material = models.CharField(max_length=255)
    bracelet_material = models.CharField(max_length=255)
    caliber = models.IntegerField()
    gender = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class WatchType(models.Model):
    watch = models.ForeignKey(Watch, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2, validators=[
        MinValueValidator(0)
    ],)
    worth = models.DecimalField(max_digits=9, decimal_places=2, validators=[
        MinValueValidator(0.00)
    ],)

    def __str__(self):
        return f'{self.type.name} [{self.watch.name}]'
