from django.db import models
from django.conf import settings
from Recipes.models import Recipe  # Use absolute import for cross-app model reference

class MealPlan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    meal_type = models.CharField(
        max_length=10,
        choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner')]
    )
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'date', 'meal_type')

    def __str__(self):
        return f"{self.user} - {self.date} - {self.meal_type}"
