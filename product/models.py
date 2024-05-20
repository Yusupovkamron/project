from django.db import models
from cakes.models import Sweets, Locations

class Products(models.Model):
    title = models.CharField(max_length=500)
    name = models.CharField(max_length=400)
    sweets = models.ForeignKey(Sweets, on_delete=models.CASCADE)
    reklama = models.URLField(null=True, blank=False)
    image = models.ImageField(upload_to="product/products")
    locations = models.ManyToManyField(Locations)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"{self.sweets}"


class Services(models.Model):
    title = models.CharField(max_length=400)
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="cakes/masters/")
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    text = models.TextField()
    customer = models.ForeignKey(Services, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:10]
