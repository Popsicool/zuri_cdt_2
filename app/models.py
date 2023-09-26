from django.db import models

# Create your models here.

class Club(models.Model):
    name = models.CharField(max_length=250)
    age = models.PositiveIntegerField()
    bio = models.TextField()

    def __str__(self):
        return f"{self.age} - {self.age}"