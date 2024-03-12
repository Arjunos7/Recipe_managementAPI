from django.db import models
class Recipe(models.Model):
    name=models.CharField(max_length=300)
    ingredients=models.TextField()
    cuisine=models.CharField(max_length=200)
    meal_type=models.CharField(max_length=300)
    created_at=models.DateTimeField(auto_now_add=True)
    edited_at=models.DateTimeField(auto_now_add=True)
    rating=models.IntegerField(null=True,blank=True)
    comment=models.CharField(max_length=300)

    def __str__(self):
        return self.name
