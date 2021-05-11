from django.contrib import admin
# from apps.productApp.models import Category, SubCategory, Product, SizeVariation, ColourVariation, Formula, Ingredients, IngredientsHistory
from apps.productApp.models import Category, SubCategory, Product, Formula, Ingredients, IngredientsHistory

# Register your models here.



admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
# admin.site.register(ColourVariation)
# admin.site.register(SizeVariation)
admin.site.register(Formula)
admin.site.register(Ingredients)
admin.site.register(IngredientsHistory)
