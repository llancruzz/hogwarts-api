# Import necessary modules
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Post, Like
from .serializers import LikeSerializer

User = get_user_model()


class LikeListViewTestCase(APITestCase):
    """
    Like list test:
    List likes authenticate users.
    List likes unauthenticated users.
    """

    def setUp(self):
        self.owner = User.objects.create_user('alan', password='testpass')
        self.post = Post.objects.create(
            owner=self.owner,
            title='Test Post',
            content='Testing like post'
        )
        self.like1 = Like.objects.create(
            post=self.post,
            owner=self.owner
        )

    def test_list_likes_authenticated_user(self):
        url = reverse('like-list')
        self.client.force_authenticate(user=self.owner)
        response = self.client.get(url)
        likes = Like.objects.filter(owner=self.owner)
        serializer = LikeSerializer(likes, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_list_likes_unauthenticated_user(self):
        url = reverse('like-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_like_string_representation(self):
        user = User.objects.create_user(username='harry')
        post = Post.objects.create(
            owner=user, title='test post', content='test content')
        like = Like.objects.create(owner=user, post=post)

        expected_str = f'{user} {post}'
        self.assertEqual(str(like), expected_str)

    def test_duplicate_likes_should_not_be_allowed(self):
        """Test a duplicate like cannot be created"""

        self.client.login(username="alan", password='testpass')
        response = self.client.post(
            "/likes/",
            {
                "post": self.post.id,
            },
        )
        self.assertEqual(response.data, {'detail': 'Possible duplicate'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
