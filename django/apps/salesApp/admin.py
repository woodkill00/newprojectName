from django.contrib import admin
from apps.salesApp.models import Position, Sale, CSV

# Register your models here.

admin.site.register(Position)
admin.site.register(Sale)
admin.site.register(CSV)