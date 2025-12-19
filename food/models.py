from django.db import models

class FoodType(models.Model):
    type = models.CharField(max_length=50)
    def __str__(self):
        return self.type

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_good = models.ImageField(upload_to='')
    image_bad = models.ImageField(upload_to='')
    how_to_analyze = models.TextField()
    type = models.ForeignKey(FoodType, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} tipo {self.type}'