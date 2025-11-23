from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Items(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE, related_name='items')
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name