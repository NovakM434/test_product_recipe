from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.db.models import Q

from .models import Recipe, Product, RecipeProduct


def add_product_to_recipe(request, recipe_id, product_id, weight):
    product = Product.objects.get(id=product_id)
    recipe = Recipe.objects.get(id=recipe_id)
    recipe_product = RecipeProduct.objects.filter(recipe=recipe, product=product)
    recipe_product, created = RecipeProduct.objects.get_or_create(
        recipe=recipe,
        product=product,
        defaults={'weight': weight}
    )
    if not created:
        recipe_product.weight = weight
        recipe_product.save()
        return HttpResponse('Вы обновили вес продукта в рецепте.')
    else:
        return HttpResponse('Рецепт создан.')


def cook_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe_products = RecipeProduct.objects.filter(recipe=recipe)

    for recipe_product in recipe_products:
        product = recipe_product.product
        product.count += 1
        product.save()

    return HttpResponse('Рецепт приготовлен.')


def show_recipes_without_product(request, product_id):
    product = Product.objects.get(id=product_id)

    recipes_without_product = Recipe.objects.exclude(
        Q(recipes_products__product=product) & Q(recipes_products__weight__gte=10)
    )
    return render(request, 'recipes_without_product.html', {'recipes': recipes_without_product})
