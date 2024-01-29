from django.db import models

from django.core.validators import RegexValidator


class Product(models.Model):
    name = models.CharField(
        verbose_name="Наименование продукта",
        max_length=200,
        unique=True,
        blank=False,
        null=False
    )
    count = models.IntegerField(
        verbose_name="Сколько раз был использован в рецепте",
        default=0
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.name}"


class Recipe(models.Model):
    name = models.CharField(
        verbose_name="Название рецепта",
        max_length=200,
        unique=True,
        blank=False,
        null=False,
        validators=[
            RegexValidator(
                regex="^(?=.*[a-zA-Z\u0400-\u04FF]).+$",
                message="Нельзя создавать рецепт только из цифр или знаков"
            )
        ]
    )
    product = models.ManyToManyField(
        Product,
        through="RecipeProduct",
        related_name="recipes",
        verbose_name="Продукты",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"


class RecipeProduct(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name="Рецепт",
        related_name="recipes_products",
        help_text="Укажите рецепт"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Продукты",
        related_name="recipes_products",
        help_text="Выберите продукты"
    )
    weight = models.FloatField(
        verbose_name="Количество грамм",
        blank=False,
        null=False
    )

    def __str__(self):
        return (
            f"Продукты для для {self.recipe}: {self.product}:{self.weight}"
        )
