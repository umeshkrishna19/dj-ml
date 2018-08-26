from django.urls import path, include
from . import views

app_name = 'predictions'
urlpatterns = [
    path('', views.PredictionsView.as_view(), name='view-all'),
    path('add', views.PredictionsAdd.as_view(), name='add'),
]