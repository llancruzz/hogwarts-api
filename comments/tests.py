# Importing necessary modules
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
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
        # Create a test client and a user for the tests
        self.client = APIClient()
        User.objects.create_user(username="alan", password="test")
        # Define the URL for the comment list view
        self.url = "/comments/"

    def test_can_list_comments(self):
        # Create a post and retrieve the comments using GET request
        alan = User.objects.get(username="alan")
        Post.objects.create(owner=alan, content="testing comment")
        response = self.client.get("/comments/")
        # Assert that the response status code is HTTP_200_OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Print the response data and its length for debugging purposes
        print(response.data)
        print(len(response.data))

    def test_user_create_comment(self):
        # Create a user and post to be used in the test
        alex = User.objects.create_user(username="alex", password="test")
        post = Post.objects.create(owner=alex, content="testing comment")
        # Log in with the test user
        self.client.login(username="alex", password="test")
        # Define the data to be posted
        data = {"content": "Test comment", "post": post.id}
        # Post the data to the comment list view using the test client
        response = self.client.post(self.url, data, format="json")
        # Assert that the response status code is HTTP_201_CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Assert that a comment was created
        self.assertEqual(Comment.objects.count(), 1)
        # Retrieve the comment and assert that its attributes
        # match the data posted
        comment = Comment.objects.first()
        self.assertEqual(comment.content, "Test comment")
        self.assertEqual(comment.post.id, post.id)
        self.assertEqual(comment.owner, alex)
        # Print the response content for debugging purposes
        print(response.content.decode("utf-8"))

    def test_logged_out_user_cant_create_comment(self):
        # Attempt to post a comment without logging in
        response = self.client.post("/comments/", {"content": "testing"})
        # Assert that the response status code is HTTP_403_FORBIDDEN
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
        # Create test users
        self.alan = User.objects.create_user(
            username="alan", password="testpass")
        self.alex = User.objects.create_user(
            username="alex", password="testpass")
        # Create test posts
        self.post = Post.objects.create(
            owner=self.alan, title="testing alan", content="alan's content"
        )
        self.post = Post.objects.create(
            owner=self.alex, title="testing alex", content="alex's content"
        )
        # Create test comments
        self.comment = Comment.objects.create(
            owner=self.alan, post=self.post, content="test comment"
        )
        self.comment = Comment.objects.create(
            owner=self.alex, post=self.post, content="test comment"
        )

    def test_can_retrieve_comment_using_valid_id(self):
        # Test that a user can retrieve a comment with a valid id
        url = reverse("comment-detail", args=[self.comment.id])
        response = self.client.get(url)
        self.assertEqual(response.data["content"], "test comment")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_comment_using_invalid_id(self):
        # Test that a user can't retrieve a comment with an invalid id
        response = self.client.get("/comment-detail/555/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_comment(self):
        # Test that a user can update their own comment
        self.client.login(username="alan", password="testpass")
        url = reverse("comment-detail", args=[self.comment.id])
        response = self.client.get(url)
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.content, "alan's content")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_comment(self):
        # Test that a user can't update another user's comment
        self.client.login(username="alan", password="testpass")
        response = self.client.put("/posts/2/", {"content": "alex's content"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CommentModelTestCase(APITestCase):
    """
    Comment model test"
    Test __str__()
    """

    def test_comment_string_representation(self):
        # Test that a comment is represented as a string correctly
        user = User.objects.create(username="testuser")
        post = Post.objects.create(
            title="test post", content="test content", owner=user
        )
        comment = Comment.objects.create(
            owner=user, post=post, content="test comment")
        expected_string = "test comment"
        self.assertEqual(str(comment), expected_string)
