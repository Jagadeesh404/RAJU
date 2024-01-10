from django.db import models

# Create your models here.
class Hydjobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=90)
    title = models.CharField(max_length=90)
    eligibility = models.CharField(max_length=90)
    address = models.CharField(max_length=910)
    email = models.EmailField()
    number = models.BigIntegerField()

class Apjobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=90)
    title = models.CharField(max_length=90)
    eligibility = models.CharField(max_length=90)
    address = models.CharField(max_length=910)
    email = models.EmailField()
    number = models.BigIntegerField()

class Kajobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=90)
    title = models.CharField(max_length=90)
    eligibility = models.CharField(max_length=90)
    address = models.CharField(max_length=910)
    email = models.EmailField()
    number = models.BigIntegerField()