from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnail/')

    def __str__(self):
        return self.name
