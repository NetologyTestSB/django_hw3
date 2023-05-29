from django.db import models

from datetime import datetime


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products')
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50)

    def normal_date(self):
        return self.release_date.strftime('%d.%m.%Y')

    def __str__(self):
        return self.name
