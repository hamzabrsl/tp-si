from django.contrib import admin

from .models import product, Ingredient, Category

admin .site.register(product)
admin .site.register(Ingredient)
admin .site.register(Category)

