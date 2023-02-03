from django.db import models

# Create your models here.
class createSellers(models.Model):
    fullname=models.CharField(max_length=500)
    adress=models.CharField(max_length=500)
    phonenum=models.CharField(max_length=15)
    def __str__(self):
        return self.fullname
    



class CreateProduct(models.Model):
    name=models.CharField(max_length=400)
    price=models.CharField(max_length=100)
    full_detail=models.TextField()
    images=models.ImageField(upload_to ='uploads/')
    def __str__(self):
        return self.name