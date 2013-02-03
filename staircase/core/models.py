from django.db import models
from model_utils import Choices


RACES = Choices('Protoss', 'Terran', 'Zerg')
CATEGORIES = Choices('macro', 'micro', 'both')


class Step(models.Model):
    number = models.IntegerField()
    race = models.IntegerField(choices=RACES)
    category = models.IntegerField(choices=CATEGORIES)


class Unit(models.Model):
    name = models.CharField(max_length=100)
    race = models.IntegerField(choices=RACES)
    step = models.ForeignKey(Step, blank=True, null=True)
