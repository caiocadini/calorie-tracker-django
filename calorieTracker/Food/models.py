from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=200)
    portion_weight_in_grams = models.IntegerField(default=0)
    calories_per_portion_in_grams = models.IntegerField(default=0)
    protein_per_portion_in_grams = models.IntegerField(default=0)
    carbs_per_portion_in_grams = models.IntegerField(default=0)
    fat_per_portion_in_grams = models.IntegerField(default=0)
    fibers_per_portion_in_grams = models.IntegerField(default=0)