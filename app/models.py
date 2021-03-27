from django.db import models

# Create your models here.
class Player(models.Model):
    first_name=models.CharField(max_length=50)
    middle_name=models.CharField(max_length=50,blank=True)
    last_name=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    club=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name}-{self.middle_name}-{self.last_name}"
