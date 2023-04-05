# Import necessary modules
from django.db import models
from django.contrib.auth.models import User


# Define Contact model
class Contact(models.Model):
    """
    Contact model, related to User.
    Users are able to report any issues with the application.
    """

    # Define fields for the Contact model
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    reason_contact = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)

    # Define meta options for the Contact model
    class Meta:
        ordering = ["-created_at"]

    # Define string representation of the Contact model
    def __str__(self):
        return f"{self.owner} {self.reason_contact}"
