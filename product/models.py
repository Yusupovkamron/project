from django.db import models
from cakes.models import Sweets, Locations

class Products(models.Model):
    sweets = models.ForeignKey(Sweets, on_delete=models.CASCADE)
    reklama = models.URLField(null=True, blank=False)
    image = models.ImageField(upload_to="product/products")
    locations = models.ManyToManyField(Locations)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.sweets}"


