from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100)
    branches = models.IntegerField(max_length=10)
    def __str__(self):
        return self.name

class resturanttype(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class foodtype(models.Model):
    name = models.CharField(max_length=100)
    resurant = models.ForeignKey(resturanttype, on_delete=models.CASCADE)
    price = models.IntegerField()
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class places(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    resturant = models.ForeignKey(resturanttype, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.resturant.name

class food(models.Model):
    resturant = models.ForeignKey(resturanttype, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.resturant.name

class profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class comments(models.Model):
    user = models.ForeignKey(profile, on_delete=models.CASCADE)
    resturant = models.ForeignKey(resturanttype, on_delete=models.CASCADE)
    food = models.ForeignKey(foodtype, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.resturant.name
