# Import necessary modules
from rest_framework import generics, permissions
from hogwarts_api.permissions import IsOwnerOrReadOnly
from .models import Contact
from .serializers import ContactSerializer


class ContactList(generics.ListCreateAPIView):
    """
    ContactList generic view:
    List all contact or create a contact if logged in.
    """

    serializer_class = ContactSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Contact.objects.all()

    def perform_create(self, serializer):
        """
        Override the perform_create method to set the owner of
        the contact to the currently authenticated user.
        """
        serializer.save(owner=self.request.user)


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    ContactDetail generic view:
    Retrieve a contact, or update or delete it by id if you own it.
    """

    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Contact.objects.all()
