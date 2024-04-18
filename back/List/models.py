from django.db import models

# Create your models here.
class Food(models.Model):
    Title = models.CharField(max_length=120)
    Ingredients = models.TextField()

    def _str_(self):
        return self.title