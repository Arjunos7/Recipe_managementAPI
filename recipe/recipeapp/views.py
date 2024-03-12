from django.shortcuts import render
from rest_framework import viewsets
from recipeapp.serializers import RecipeSerializer,UserSerializer
from recipeapp.models import Recipe
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q


class Recipe_details(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated,]


class CreateUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class user_logout(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        self.request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)



class Search(APIView):
    def get(self,request):
        query=self.request.query_params.get('search')
        if(query):
            recipe=Recipe.objects.filter(Q(name__icontains=query) | Q(ingredients__icontains=query) | Q(cuisine__icontains=query) | Q(meal_type__icontains=query))
            r=RecipeSerializer(recipe,many=True)
            return Response(r.data)




