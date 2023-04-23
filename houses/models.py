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


@receiver(post_save, post_delete, sender=Like)
def update_house_points(instance, created, **kwargs):
    """Create or update the house points"""
    # Get the house name from the post in the like
    house = instance.post.house
    # Get the house whose points need updating
    house_to_update, created = HouseProfile.objects.get_or_create(
        house_name=house)
    # Set points as current total
    if created:
        house_to_update.current_points = 0
    else:
        likes_count = Like.objects.filter(post__house=house).count()
        house_to_update.current_points = likes_count
    house_to_update.save()
