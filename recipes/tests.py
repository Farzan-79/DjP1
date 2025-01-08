from django.test import TestCase
from django.contrib.auth import get_user_model
from recipes.models import Recipe, RecipeIngredients
from django.contrib.auth import login

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
            recipe = self.recipe_a
        )

        self.ingredients_a2 = RecipeIngredients.objects.create(
            name = 'sugar',
            recipe = self.recipe_a
        )

        self.ingredients_a3 = RecipeIngredients.objects.create(
            name = 'butter',
            recipe = self.recipe_a
        )

    
    def test_user_ing(self):
        my_user = User.objects.get(username= 'a')
        my_recipe = my_user.recipe_set.get(name= 'pancake')
        my_ings = my_recipe.ings.all()
        ings = {ing.name for ing in my_ings}
        self.assertEqual(ings, {'milk', 'sugar', 'butter'})

    def test_ing_user(self):
        ing = RecipeIngredients.objects.get(id=1)
        user = ing.recipe.user.username
        self.assertEqual(user, 'a')

    def test_two_level(self):
        ing = RecipeIngredients.objects.filter(recipe__user__username= 'a')
        self.assertEqual(3, ing.count())

    def test_reverse_two_level(self):
        user = User.objects.get(recipe__ings__name = 'milk')
        self.assertEqual(user, self.user_a)

    def test_another(self):
        user = self.user_a
        riids = user.recipe_set.all().values_list('ings__name', flat=True)
        print(set(riids))

