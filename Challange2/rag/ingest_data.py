# kitchen_buddy/utils.py

import json
from .models import Recipe, Ingredient, RecipeIngredient

def load_and_combine_recipes(json_file_path, output_file_path):
    existing_recipes = Recipe.objects.all()
    existing_data = []

    for recipe in existing_recipes:
        ingredients = RecipeIngredient.objects.filter(recipe=recipe)
        ingredient_list = [
            {
                'name': ingredient.ingredient.name,
                'quantity': ingredient.quantity,
                'unit': ingredient.unit
            }
            for ingredient in ingredients
        ]
        existing_data.append({
            'name': recipe.name,
            'ingredients': ingredient_list,
            'instructions': recipe.instructions,
            'taste': recipe.taste,
            'cuisine_type': recipe.cuisine_type,
            'preparation_time': recipe.preparation_time,
            'reviews': recipe.reviews
        })

  
    with open(json_file_path) as f:
        new_recipes = json.load(f)
        for recipe_data in new_recipes:
            recipe = Recipe.objects.create(
                name=recipe_data['name'],
                instructions=recipe_data['instructions'],
                taste=recipe_data['taste'],
                cuisine_type=recipe_data['cuisine_type'],
                preparation_time=recipe_data['preparation_time'],
                reviews=5
            )
            for ingredient_data in recipe_data['ingredients']:
                ingredient, created = Ingredient.objects.get_or_create(
                    name=ingredient_data['name']
                )
                RecipeIngredient.objects.create(
                    recipe=recipe,
                    ingredient=ingredient,
                    quantity=ingredient_data['quantity'],
                    unit=ingredient_data['unit']
                )
            existing_data.append(recipe_data)

    with open(output_file_path, 'w') as outfile:
        json.dump(existing_data, outfile, indent=4)
