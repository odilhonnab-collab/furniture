from django.urls import path
from .views import feedback_page

urlpatterns = [
    path("", feedback_page, name="feedback"),
]