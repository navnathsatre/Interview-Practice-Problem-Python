from django.db import models

# Create your models here.
class Employee(models.model):
    empid = models.IntegerField()
    empname =  models.CharField(max_length=100)
    registered_date = models.DateTimeField()
