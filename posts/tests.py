from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post


class PostListViewTests(APITestCase):
    """
    PostList view tests:
    User can list all the posts.
    Logged in user can create a post.
    Logged out user can't create a post.
    """

    # Method setUp() that will automatically run before every test method in the class.
    def setUp(self):
        User.objects.create_user(username='alan', password='test')

    def test_can_list_posts(self):
        alan = User.objects.get(username='alan')
        Post.objects.create(owner=alan, title='brazilian')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    # Method client.login() APITest client : To test protected routes
    def test_logged_in_user_can_create_post(self):
        self.client.login(username='alan', password='test')
        response = self.client.post('/posts/', {'title': 'brazilian'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cant_create_post(self):
        response = self.client.post('/posts/', {'title': 'brazilian'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
