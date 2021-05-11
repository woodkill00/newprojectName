from django.urls import path
from apps.newsReaderApp import views


app_name = 'newsReaderApp'

urlpatterns = [
    path('', views.home, name="Home"),
    path('next', views.loadcontent, name="Loadcontent"),
]