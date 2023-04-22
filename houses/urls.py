# Import necessary modules
from django.urls import path
from houses import views

urlpatterns = [
    path("houses/", views.HouseProfileList.as_view()),
    path("houses/<int:pk>/", views.HouseProfileDetail.as_view()),
]
