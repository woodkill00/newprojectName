from django.urls import path
from .views import HomeView
# from apps.userApp

app_name = 'apps.mainApp'

urlpatterns = [
    path('', HomeView.as_view(), name='main'),
]