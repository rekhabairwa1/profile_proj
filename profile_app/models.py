from django.db import models

# Create your models here.
class my_profile(models.Model):
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    roll_no = models.IntegerField()
    stream = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=70)
    gender = models.CharField(max_length=70)
    mobile_no = models.IntegerField()
    image = models.ImageField(upload_to='media',null=True)
    description = models.CharField(max_length=400)