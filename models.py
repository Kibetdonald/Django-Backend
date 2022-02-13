from django.db import models

# Create your models here.
class Delegates(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    mationality = models.CharField(max_length=30)
   
    


