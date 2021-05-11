from django.db import models
from apps.userApp.models import UserProfile
from django.urls import reverse

# Create your models here.

class Report(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='reports', blank=True)
    remarks = models.TextField()
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("reports_app:report-detail", kwargs={"pk": self.pk})


    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = (
            '-created',
        )





