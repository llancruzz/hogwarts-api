# Import necessary modules
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Contact


# Define test cases for the Contact API
class ContactAPITest(APITestCase):
    """
    Contac tests:
    Get Contact and create contact
    """

    # Set up the test case by creating a user and contact and authenticating the client
    def setUp(self):
        self.user = User.objects.create_user(
            username='alan', password='pass')
        self.contact = Contact.objects.create(
            owner=self.user, reason_contact='Test Reason',
            content='Test Content')
        self.client.force_authenticate(user=self.user)

    # Test getting contacts
    def test_get_contacts(self):
        url = reverse('contacts')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test creating a contact
    def test_create_contact(self):
        url = reverse('contacts')
        data = {
            'owner': self.user.id,
            'reason_contact': 'Test Reason 2',
            'content': 'Test Content 2'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Test the string representation of a contact object
    def test_contact_string_representation(self):
        contact = Contact.objects.get(id=1)
        expected_string = f'{contact.owner} {contact.reason_contact}'
        self.assertEqual(str(contact), expected_string)
