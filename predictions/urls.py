from django.urls import path, include
from . import views

urlpatterns = [
    path('test/', views.test),
    path('homepage/', views.PredictionsHomePage.as_view()),
]