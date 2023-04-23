# Import necessary modules
from likes.models import Like
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User


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


@receiver(post_save, sender=Like)
@receiver(post_delete, sender=Like)
def update_house_points(instance, **kwargs):
    """Create or update the house points"""
    # Get the house name from the post in the like
    house = instance.post.house
    # Get the house whos points need updated
    house_to_update, _ = HouseProfile.objects.get_or_create(house_name=house)
    # Set points as current total +1 if like, -1 if unlike
    if instance.is_like:
        house_to_update.current_points += 1
    else:
        house_to_update.current_points -= 1
    house_to_update.save()
