from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=50)
    is_featured = models.BooleanField(default=False)
#tambahan 
    stock = models.IntegerField(default=0)
    brand = models.CharField(max_length=50, null=True, blank=True)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

