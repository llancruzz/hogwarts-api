# Importing necessary modules
from django.urls import path
from comments import views

# Defining urlpatterns for the comments app
urlpatterns = [
    # Path to list all comments and create new comments
    path('comments/', views.CommentList.as_view()),
    # Path to retrieve, update or delete a specific comment by ID
    path('comments/<int:pk>/', views.CommentDetail.as_view(),
         name='comment-detail'),
]
