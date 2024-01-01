from django.db import models

# Create your models here.
class Sect(models.Model):
    name = models.CharField(max_length=200)
    justice = models.BooleanField()

class Creature(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    sex = models.IntegerField()

    class Meta:
        abstract = True

class SpiritualCreature(Creature):
    
    taoist_name = models.CharField(max_length=200)
    realm = models.BigIntegerField(default=0)
    spiritual_power = models.BigIntegerField(default=0)
    kindness = models.BigIntegerField(default=0)
    spiritual_root = models.TextField()

    class Meta:
        abstract = True

class Humanoid(SpiritualCreature):
    sect = models.ForeignKey(to=Sect,on_delete=models.SET_NULL,blank=True)

class User(models.Model):
    uid = models.CharField(max_length=100)
    sign_date = models.DateField()
    icon = models.TextField(null=True,default=None)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    container_type = models.CharField(max_length=32)
    container_id = models.IntegerField()
    