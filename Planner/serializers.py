from rest_framework import serializers
from Planner.models import MealPlan
from Recipes.models import Recipe  # to serialize recipe details

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class MealPlanSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer(read_only=True)
    recipe_id = serializers.PrimaryKeyRelatedField(
        queryset=Recipe.objects.all(),
        source='recipe',
        write_only=True
    )

    class Meta:
        model = MealPlan
        fields = ['id', 'user', 'date', 'meal_type', 'recipe', 'recipe_id']
