from django.urls import path

from apps.updateServerApp import views

app_name = 'updateServerApp'

urlpatterns = [
    path("updateServer/", views.update, name="update-server"),
]