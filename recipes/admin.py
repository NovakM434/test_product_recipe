from django.contrib import admin

from .models import Recipe, RecipeProduct, Product


@admin.register(Recipe)
class Recipeadmin(admin.ModelAdmin):

    list_display = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('id',)
    empty_value_display = '-Пусто-'


@admin.register(RecipeProduct)
class RecipeProduct(admin.ModelAdmin):
    list_display = ('id', 'recipe', 'product', 'weight')
    ordering = ('id',)
    empty_value_display = '-Пусто-'


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('id', 'name', 'count')
