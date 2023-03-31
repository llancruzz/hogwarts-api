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


class PostDetailViewTests(APITestCase):
    """
    PostDetail view tests:
    User can retrieve a post with a valid id.
    User can't retrieve a post with an invalid id
    Users can update the posts they own
    Users can't update the posts they don't own
    """

    # Create two users and two posts for each user.
    def setUp(self):
        alan = User.objects.create_user(username='alan', password='test')
        alex = User.objects.create_user(username='alex', password='test')
        Post.objects.create(
            owner=alan, title='brazilian', content='alans content'
        )
        Post.objects.create(
            owner=alex, title='another brazilian', content='alexs content'
        )

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'brazilian')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        response = self.client.get('/posts/555/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        self.client.login(username='alan', password='test')
        response = self.client.put('/posts/1/', {'title': 'irish'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'irish')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_post(self):
        self.client.login(username='alan', password='test')
        response = self.client.put('/posts/2/', {'title': 'irish'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
