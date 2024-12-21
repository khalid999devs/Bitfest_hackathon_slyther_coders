from django.http import JsonResponse
from .fine_tune import fine_tune_model
from .ingest_data import load_and_combine_recipes
from .chat import initialize_chat, chat_with_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Ingredient
from .serializer import IngredientSerializer,RecipeSerializer,RecipeIngredientSerializer
from rest_framework import status
import os
from newproject.settings import BASE_DIR


chat_chain = initialize_chat()  # Initialize the chat chain globally

# Ingredients
@api_view(['GET'])
def get_Ingredients(request):
    allIngredients=Ingredient.objects.all()
    Ingserializer=IngredientSerializer(allIngredients,many=True)
    return Response(Ingserializer.data)

@api_view(['POST'])
def input_Ingredients(request):
 serializer=IngredientSerializer(data=request.data)
 if serializer.is_valid():
   serializer.save()
   return Response(serializer.data,status=status.HTTP_201_CREATED)
 return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def Ingredient_details(request,pk):
 try:
  ingredient=Ingredient.objects.get(pk=pk)
 except Ingredient.DoesNotExist:
  return Response(status=status.HTTP_404_NOT_FOUND)
 
 if request.method=='GET':
  serializer=IngredientSerializer(ingredient)
  return Response(serializer.data)
 
 elif request.method=='PUT':
  serializer=IngredientSerializer(ingredient,data=request.data)
  if serializer.is_valid():
   serializer.save()
   return Response(serializer.data)
  return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
 
 elif request.method=='DELETE':
  ingredient.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)
 
@api_view(['POST'])
def input_Recipe(request):
 serializer=RecipeSerializer(data=request.data)
 if serializer.is_valid():
   serializer.save()
   return Response(serializer.data,status=status.HTTP_201_CREATED)
 return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def retrive_recipes(request):
    try:
        input_file = os.path.join(BASE_DIR, 'rag', 'data.json')
        output_file = 'my_fav_recipes.txt'
        load_and_combine_recipes(input_file, output_file)
        return Response({"message": "Recipies tuned successfully"})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@api_view(['POST'])
def chat(request):
    user_input = request.GET.get('user_input')
    if not user_input:
        return JsonResponse({"error": "No user input provided"}, status=400)

    try:
        response = chat_with_model(chat_chain, user_input)
        return JsonResponse({"response": response})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)