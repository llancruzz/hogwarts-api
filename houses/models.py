# Import necessary modules
from django.db import models


# Define House Profile models here.
class HouseProfile(models.Model):
    """
    House profile model.
    """
    house_name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    current_points = models.IntegerField(default=0)

    def __str__(self):
        return self.house_name
