# Import necessary modules
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Follower
from .serializers import FollowerSerializer
from rest_framework.exceptions import ValidationError
from django.db import IntegrityError


class FollowerListViewTestCase(APITestCase):
    """
    Follower list test:
    List followers authenticate users.
    List followers unauthenticated users.
    """

    def setUp(self):
        self.user1 = User.objects.create_user(
            username="alan", password="password1")
        self.user2 = User.objects.create_user(
            username="alex", password="password1")
        self.user1.save()
        self.user2.save()

        self.client.force_authenticate(user=self.user1)
        self.url = reverse("follow-list")

    def test_follow_list_view_authenticated(self):
        # Test that an authenticated user can retrieve a list of followers
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

        # Follow another user
        follow = Follower.objects.create(owner=self.user1, followed=self.user2)
        # print(follow.owner, follow.followed)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
        self.assertIn("alan", [f["owner"] for f in response.data["results"]])
        self.assertIn(self.user2.id, [f["followed"]
                      for f in response.data["results"]])

    def test_create_follower_view_authenticated(self):
        # Test that an authenticated user can create a follower
        data = {"owner": self.user1.username, "followed": self.user2.id}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["owner"], "alan")
        self.assertEqual(response.data["followed"], self.user2.id)

    def test_str_method(self):
        self.follower = Follower.objects.create(
            owner=self.user1, followed=self.user2)
        self.assertEqual(str(self.follower), f"{self.user1} {self.user2}")
