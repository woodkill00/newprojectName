from django.db.models.deletion import CASCADE, SET_NULL
from apps.userApp.models import CustomUser
# from cart.models import Product
from django.db import models
from django.contrib.auth import get_user_model
from apps.productApp.models import Product, Category

User = get_user_model()

# Create your models here.

# class Category(models.Model):
#     name = models.CharField(max_length=100)

#     class Meta:
#         verbose_name_plural = "Categories"

#     def __str__(self):
#         return self.name



class Stock(models.Model):
    # category = models.CharField(max_length=50, blank=True, null=True)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50, blank=True, null=True)
    # product_name = models.ForeignKey(Product, blank=True, null=True, on_delete=CASCADE)
    product_name = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(default='0', blank=True, null=True)
    received_quantity = models.IntegerField(default='0', blank=True, null=True)
    # received_by = models.CharField(max_length=50, blank=True, null=True)
    received_by = models.ForeignKey(CustomUser, related_name='received_by', unique=False, on_delete=models.CASCADE)
    issued_quantity = models.IntegerField(default='0', blank=True, null=True)
    issued_by = models.ForeignKey(CustomUser, related_name='issued_by', on_delete=models.CASCADE)
    # issued_by = models.CharField(max_length=50, blank=True, null=True)
    issued_to = models.ForeignKey(CustomUser, related_name='issued_to', on_delete=models.CASCADE)
    # issued_to = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.ForeignKey(CustomUser, related_name='created_by', on_delete=models.CASCADE)
    # created_by = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=SET_NULL)
    # created_by = models.CharField(max_length=50, blank=True, null=True)
    reorder_level = models.IntegerField(default='0', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    export_to_CSV = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Stocks"


    def __str__(self):
        # return self.item_name
        return self