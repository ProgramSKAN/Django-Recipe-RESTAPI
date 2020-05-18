from rest_framework import viewsets,mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag,Ingredient,Recipe
from recipe import serializers

class BaseRecipeAttrViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin):
    """Base viewset for user owned recipe attributes"""
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')
    def perform_create(self,serializer):
        """Create a new object"""
        serializer.save(user=self.request.user)

class TagsViewSet(BaseRecipeAttrViewSet):
    """Manage Tags in the Database"""
    queryset=Tag.objects.all()
    serializer_class=serializers.TagSerializer

class IngredientsViewSet(BaseRecipeAttrViewSet):
    """Manage Ingredients in the Database"""
    queryset=Ingredient.objects.all()
    serializer_class=serializers.IngredientSerializer


##below is unrefactored code of above
# class TagsViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin):
#     """Manage Tags in the Database"""
#     authentication_classes=(TokenAuthentication,)
#     permission_classes=(IsAuthenticated,)
#     queryset=Tag.objects.all()
#     serializer_class=serializers.TagSerializer

#     def get_queryset(self):
#         """Return objects for the current authenticated user only"""
#         return self.queryset.filter(user=self.request.user).order_by('-name')

#     def perform_create(self,serializer):
#         """Create a new tag"""
#         serializer.save(user=self.request.user)

# class IngredientsViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin):
#     """Manage Ingredients in the Database"""
#     authentication_classes=(TokenAuthentication,)
#     permission_classes=(IsAuthenticated,)
#     queryset=Ingredient.objects.all()
#     serializer_class=serializers.IngredientSerializer

#     def get_queryset(self):
#         """Return objects for the current authenticated user only"""
#         return self.queryset.filter(user=self.request.user).order_by('-name')

#     def perform_create(self,serializer):
#         """Create a new ingredient"""
#         serializer.save(user=self.request.user)


class RecipeViewSet(viewsets.ModelViewSet):
    """Manage recipes in the Database"""
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    queryset=Recipe.objects.all()
    serializer_class=serializers.RecipeSerializer

    def get_queryset(self):
        """retrive the recipes for the authenticated user"""
        return self.queryset.filter(user=self.request.user)
    
    def get_serializer_class(self):
        """return appropriate serializer class"""
        if self.action=='retrieve':
            return serializers.RecipeDetailSerializer
        
        return self.serializer_class

    def perform_create(self,serializer):
        """Create a new recipe"""
        serializer.save(user=self.request.user)


