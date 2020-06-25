from django.db import models


# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    img = models.ImageField(upload_to='pics')
