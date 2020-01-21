from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=64)
    price1  = models.IntegerField()
    price2 = models.IntegerField()
    discount = models.IntegerField()
    image = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.name