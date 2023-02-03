from django.db import models

# Create your models here.
class orders(models.Model):
    product=models.ForeignKey("products.CreateProduct", on_delete=models.CASCADE)
    customernum=models.CharField(max_length=12)
    def __str__(self):
        return self.customernum