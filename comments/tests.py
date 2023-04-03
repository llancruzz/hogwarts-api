from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Comment, Post
from django.urls import reverse


class CommentListViewTests(APITestCase):
    """
    CommentList view tests:
    User can list all the comments.
    Logged in user can create a comment.
    Logged out user can't create a comment.
    """

    def setUp(self):
        User.objects.create_user(username='alan', password='test')

    def test_can_list_comments(self):
        alan = User.objects.get(username='alan')
        Post.objects.create(owner=alan, content='testing comment')
        response = self.client.get('/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_out_user_cant_create_comment(self):
        response = self.client.post('/comments/', {'content': 'testing'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CommentDetailViewTests(APITestCase):
    """
    CommentDetail view tests:
    User can retrieve a comment with a valid id.
    User can't retrieve a comment with an invalid id
    Users can update the comments they own
    Users can't update the comments they don't own
    """

    def setUp(self):
        self.alan = User.objects.create_user(
            username='alan', password='testpass')
        self.alex = User.objects.create_user(
            username='alex', password='testpass')
        self.post = Post.objects.create(
            owner=self.alan, title='testing alan', content='alan\'s content'
        )
        self.comment = Comment.objects.create(
            owner=self.alan, post=self.post, content='test comment'
        )

    def test_can_retrieve_comment_using_valid_id(self):
        url = reverse('comment-detail', args=[self.comment.id])
        response = self.client.get(url)
        self.assertEqual(response.data['content'], 'test comment')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_comment_using_invalid_id(self):
        response = self.client.get('/comment-detail/555/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        self.client.login(username='alan', password='test')
        response = self.client.put('/posts/1/', {'title': 'irish'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'irish')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
