from django.db import models

# Create your models here.
class Dishes(models.Model):
    name=models.CharField(max_length=120)
    price=models.PositiveIntegerField()
    category=models.CharField(max_length=120)
    rating=models.FloatField()
    def __str__(self):
        return self.name
#Dishes.objects.create(name="vb",price=120,category="veg",rating=4)
#Dishes.objects.create(name="cb",price=160,category="non veg",rating=5)
#Dishes.objects.create(name="noodles",price=180,category="non veg",rating=4)
#Dishes.objects.create(name="dosa",price=45,category="veg",rating=5)
#Dishes.objects.create(name="gheeroast",price=65,category="veg",rating=4)
#Dishes.objects.create(name="nan",price=34,category="veg",rating=5)
#Dishes.objects.create(name="mandhi",price=150,category="non veg",rating=4)
