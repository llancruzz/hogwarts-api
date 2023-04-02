from django.urls import path
from contacts import views


urlpatterns = [
    path('contacts/', views.ContactList.as_view()),
]
