from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields.related import ForeignKey
from django.db import models
from django.db.models.signals import pre_save
from django.shortcuts import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

# User = get_user_model()
from apps.userApp.models import CustomUser
# from inventoryManagement_app.models import Category
User = CustomUser

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "SubCategories"

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name

# class ColourVariation(models.Model):
#     name = models.CharField(max_length=50)

#     class Meta:
#         verbose_name_plural = "Colour Variations"

#     def __str__(self):
#         return self.name


# class SizeVariation(models.Model):
#     name = models.CharField(max_length=50)

#     class Meta:
#         verbose_name_plural = "Size Variations"

#     def __str__(self):
#         return self.name

class Product(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='product_images')
    description = models.TextField()
    price = models.IntegerField(default=0, help_text=_('in US dollars $'))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    has_colours = models.BooleanField(blank=False, default=False)
    # available_colours = models.ManyToManyField(ColourVariation, blank=False, default=None,)
    has_sizes = models.BooleanField(blank=False, default=False)
    # available_sizes = models.ManyToManyField(SizeVariation, blank=False, default=None,)
    primary_category = models.ForeignKey(
        Category, related_name='primary_products_category', blank=True, null=True, on_delete=models.CASCADE)
    secondary_categories = models.ManyToManyField(SubCategory, related_name='sub_products_category', blank=True)
    stock = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title
        # return f"{self.title}-{self.created.strftime('%d/%m/%Y')}"

    def get_absolute_url(self):
        return reverse("cart:product-detail", kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse("staff:product-update", kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse("staff:product-delete", kwargs={'pk': self.pk})

    def get_price(self):
        return "{:.2f}".format(self.price / 100)

    @property
    def in_stock(self):
        return self.stock > 0


# category_choice = (
#     ('Furniture', 'Furniture'),
#     ('IT Equipment', 'IT Equipment'),
#     ('Phone', 'Phone'),
# )

class Ingredients(models.Model):
        category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
        ingredient_category = models.CharField(max_length=50, blank=False, null=True)
        name = models.CharField(max_length=50, blank=True, null=True)
        quantity = models.IntegerField(default='0', blank=False, null=True)
        average_price_per_kilo = models.FloatField(default='', blank=True, null=True)
        received_quantity = models.IntegerField(default='0', blank=True, null=True)
        received_by = models.CharField(max_length=50, blank=True, null=True)
        issued_quantity = models.IntegerField(default='0', blank=True, null=True)
        issued_by = models.CharField(max_length=50, blank=True, null=True)
        issued_to = models.CharField(max_length=50, blank=True, null=True)
        created_by = models.CharField(max_length=50, blank=True, null=True)
        reorder_level = models.IntegerField(default='0', blank=True, null=True)
        # timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
        date_last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
        date_created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
        # date = models.DateTimeField(auto_now_add=False, auto_now=False)
        export_to_CSV = models.BooleanField(default=False)

        class Meta:
            verbose_name_plural = "Ingredients"

        def __str__(self):
            return self.name
            # return self.name + ' ' + str(self.quantity)


class IngredientsHistory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    ingredients_category = models.CharField(max_length=50, blank=False, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(default='0', blank=True, null=True)
    average_price_per_kilo = models.FloatField(default='1.0', blank=True, null=True)
    received_quantity = models.IntegerField(default='0', blank=True, null=True)
    received_by = models.CharField(max_length=50, blank=True, null=True)
    issued_quantity = models.IntegerField(default='0', blank=True, null=True)
    issued_by = models.CharField(max_length=50, blank=True, null=True)
    issued_to = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    # reorder_level = models.IntegerField(default='0', blank=True, null=True)
    # timestamp = models.DateTimeField(auto_now_add=False, auto_now=True)
    date_last_updated = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
    date_created = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
    # date = models.DateTimeField(auto_now_add=False, auto_now=False)
    # export_to_CSV = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Ingredients History"



class Formula(models.Model):
        category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
        formula_category = models.CharField(max_length=50, blank=False, null=True)
        name = models.CharField(max_length=50, blank=True, null=True)
        description = models.TextField(blank=True, null=True)
        quantity_of_ingredients = models.IntegerField(default='0', blank=False, null=True)
        # ingredients = models.ManyToManyField(Ingredients, blank=True)
        ingredient_1 = models.ForeignKey(Ingredients, blank=True, on_delete=CASCADE, related_name='ingredient_1', default='Blank', )
        ingredient_1_percentage = models.FloatField(blank=True, null=True)
        ingredient_2 = models.ForeignKey(Ingredients, blank=True, on_delete=CASCADE, related_name='ingredient_2', default='Blank')
        ingredient_2_percentage = models.FloatField(blank=True, null=True)
        ingredient_3 = models.ForeignKey(Ingredients, blank=True, on_delete=CASCADE, related_name='ingredient_3', default='Blank')
        ingredient_3_percentage = models.FloatField(blank=True, null=True)
        ingredient_4 = models.ForeignKey(Ingredients, blank=True, on_delete=CASCADE, related_name='ingredient_4', default='Blank')
        ingredient_4_percentage = models.FloatField(blank=True, null=True)
        ingredient_5 = models.ForeignKey(Ingredients, blank=True, on_delete=CASCADE, related_name='ingredient_5', default='Blank')
        ingredient_5_percentage = models.FloatField(blank=True, null=True)
        ingredient_6 = models.ForeignKey(Ingredients, blank=True, on_delete=CASCADE, related_name='ingredient_6', default='Blank')
        ingredient_6_percentage = models.FloatField(blank=True, null=True)
        ingredient_7 = models.ForeignKey(Ingredients, blank=True, on_delete=CASCADE, related_name='ingredient_7', default='Blank')
        ingredient_7_percentage = models.FloatField(blank=True, null=True)
        ingredient_8 = models.ForeignKey(Ingredients, blank=True, on_delete=CASCADE, related_name='ingredient_8', default='Blank')
        ingredient_8_percentage = models.FloatField(blank=True, null=True)
        ingredient_9 = models.ForeignKey(Ingredients, blank=True, on_delete=CASCADE, related_name='ingredient_9', default='Blank')
        ingredient_9_percentage = models.FloatField(blank=True, null=True)
        ingredient_10 = models.ForeignKey(Ingredients, blank=True, on_delete=CASCADE, related_name='ingredient_10', default='Blank')
        ingredient_10_percentage = models.FloatField(blank=True, null=True)
        # ingredient_percentage_total = join(ingredient_2_percentage + ingredient_1_percentage)
        average_price_per_kilo = models.FloatField(blank=True, null=True)
        average_cost_key_code = models.CharField(max_length=10, blank=True, null=True)
        sum = models.IntegerField(default='1000', blank=False, null=True)
        # received_quantity = models.IntegerField(default='0', blank=True, null=True)
        # received_by = models.CharField(max_length=50, blank=True, null=True)
        # issued_quantity = models.IntegerField(default='0', blank=True, null=True)
        # issued_by = models.CharField(max_length=50, blank=True, null=True)
        # issued_to = models.CharField(max_length=50, blank=True, null=True)
        created_by = models.CharField(max_length=50, blank=True, null=True)
        reorder_level = models.IntegerField(default='0', blank=True, null=True)
        # timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
        date_last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
        date_created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
        # date = models.DateTimeField(auto_now_add=False, auto_now=False)
        export_to_CSV = models.BooleanField(default=False)


        class Meta:
            verbose_name_plural = "Formulas"


        def __str__(self):
            return self.name
            # return self.name + ' ' + str(self.quantity)