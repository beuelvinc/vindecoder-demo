from django.db import models

# Create your models here.
class Vincode(models.Model):
    vin=models.CharField(max_length=150)
    model=models.CharField(max_length=150)
    make=models.CharField(max_length=150)
    rengi=models.CharField(max_length=50)
    veziyyeti=models.CharField( max_length=50)
    yan_zede=models.CharField(max_length=150)
    esas_zede=models.CharField(max_length=150)
    sekill=models.ImageField(upload_to="car_images")
    def __str__(self):
        return self.vin