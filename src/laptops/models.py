from django.db import models

# Create your models here.
class laptop(models.Model):
    name = models.CharField(max_length=100)
    brand =models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    img = models.ImageField(upload_to='laptops/images/')
    features = models.CharField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
