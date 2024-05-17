from django.db import models
# from .help import SaveMediaFile


class Sweets(models.Model):
    class PriceType(models.TextChoices):
        usd = "$"
        sum = "sum"




    name = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="cakes/sweets/")
    x_link = models.URLField(max_length=50)
    quality = models.CharField(max_length=50)
    price = models.CharField()
    price_type = models.CharField(max_length=10, choices=PriceType.choices, default=PriceType.usd)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} {self.image}"


class Discounts(models.Model):   #Discounts(chegirmalar)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cakes/discount/")
    sweet = models.ManyToManyField(Sweets, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"




class Masters(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="cakes/masters/")
    Designation = models.CharField(max_length=50)
    telegram_link = models.URLField(null=True, blank=False)
    type = models.CharField(max_length=20)
    discount = models.ManyToManyField(Discounts,  null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=False)
    imail_link = models.URLField(null=True, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Clients(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="cakes/clients/")
    title = models.CharField(max_length=300)
    clients = models.ManyToManyField(Masters,  null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"




class Locations(models.Model):
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    iphone = models.CharField(max_length=12)
    clients = models.ForeignKey(Clients, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.address} {self.email}"

