from django.test import TestCase
from django.contrib.auth import get_user_model
from recipes.models import Recipe, RecipeIngredients
from django.contrib.auth import login
from django.core.exceptions import ValidationError

# Create your tests here.

User = get_user_model()

class ForeignKeyTest(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user(username='a', password='abc123')

        self.recipe_a = Recipe.objects.create(
            name = 'pancake',
            user = self.user_a
        )

        self.ingredients_a1 = RecipeIngredients.objects.create(
            name = 'milk',
            recipe = self.recipe_a,
            quantity = '1 1/2'
            )

        self.ingredients_a2 = RecipeIngredients.objects.create(
            name = 'sugar',
            recipe = self.recipe_a,
            quantity = 10.54
        )

        self.ingredients_a3 = RecipeIngredients.objects.create(
            name = 'butter',
            recipe = self.recipe_a,
            quantity = 'abc'
        )

        self.ingredients_a4 = RecipeIngredients.objects.create(
            name = 'honey',
            recipe = self.recipe_a,
            quantity = 5/10
        )

    
    def test_user_ing(self):
        my_user = User.objects.get(username= 'a')
        my_recipe = my_user.recipe.get(name= 'pancake')
        my_ings = my_recipe.ings.all()
        ings = {ing.name for ing in my_ings}
        self.assertEqual(ings, {'milk', 'sugar', 'butter', 'honey'})

    def test_user_ing_full(self):
        user = get_user_model()
        uss = self.user_a
        ings = set(user.objects.get(id=1).recipe.values_list('ings__name', flat=True))
        #print(ings)
        self.assertEqual(ings, {'milk', 'sugar', 'butter', 'honey'})

    def test_ing_user(self):
        ing = RecipeIngredients.objects.get(id=1)
        user = ing.recipe.user.username
        self.assertEqual(user, 'a')

    def test_two_level(self):
        ing = RecipeIngredients.objects.filter(recipe__user__username= 'a')
        self.assertEqual(4, ing.count())

    def test_reverse_two_level(self):
        user = User.objects.get(recipe__ings__name = 'milk')
        self.assertEqual(user, self.user_a)

    def test_another(self):
        user = self.user_a
        riids = user.recipe.all().values_list('ings__name', flat=True)
        self.assertEqual(4 ,riids.count())

    def test_invalid_unit(self):
        invalids = ['grrr', 'nada', 'ggg']
        for i in invalids:
            with self.assertRaises(ValidationError):
                ings = RecipeIngredients(
                    name = 'n',
                    recipe = self.recipe_a,
                    quantity = 10,
                    unit = i
                )
                ings.full_clean()

    def test_valid_unit(self):
        valids = ['g', 'oz', 'kilograms', 'grams']
        for v in valids:
            ings = RecipeIngredients(
                name = 'n',
                recipe = self.recipe_a,
                quantity = 10,
                unit = v
            )
            ings.full_clean()

    def test_float_qty(self):
        self.assertEqual(self.ingredients_a1.float_quantity, 1.5)
        self.assertEqual(self.ingredients_a2.float_quantity, 10.54)
        self.assertEqual(self.ingredients_a3.float_quantity, None)
        self.assertEqual(self.ingredients_a4.float_quantity, 0.5)


