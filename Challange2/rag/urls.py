from django.urls import path
from .views import retrive_recipes,chat,get_Ingredients,input_Ingredients,Ingredient_details,input_Recipe

urlpatterns=[
  path('get-ingredients/', get_Ingredients, name='get_Ingredients'),
  path('input-ingredients', input_Ingredients, name='input_ingredients'),
  path('ingredient-details/<int:pk>',Ingredient_details,name="ingredient_details"),

  path('input-recipe', input_Recipe, name='input_Recipe'),

  
  path('retrive/', retrive_recipes, name='retrive_recipes'),
  path('chat/', chat, name='chat_with_model'),
]