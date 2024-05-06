from django.http.response import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from ..models import Recipe
from ..serializers import RecipeSerializer

@api_view()
def recipe_api_list(request):
    recipes = Recipe.objects.get_published()[:10]
    serializar = RecipeSerializer(recipes, many=True)
    return Response(serializar.data)

@api_view()
def recipe_api_detail(request, pk):
    recipes = Recipe.objects.filter(pkk=pk)
    serializar = RecipeSerializer(recipes, many=True)
    return Response(serializar.data)


