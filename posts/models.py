from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    """
    Post model, related to 'owner'. A user instance.
    Default image set to that we can always reference image.url. 
    """
    house_choices = [
        ('Gryffindor', 'Gryffindor'),
        ('Slytherin', 'Slytherin'),
        ('Ravenclaw', 'Ravenclaw'),
        ('Hufflepuff', 'Hufflepuff'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=300)
    content = models.TextField(blank=True)
    house = models.CharField(max_length=45, choices=house_choices, null=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_aypa8e', blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
