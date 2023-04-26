from django.db import models
from time import date

class recipe(models.Model):
    recipe_name=models.CharField(max_length=20)
    recipe_ingred=models.TextField(max_length=20,null=True)
    img=models.ImageField()
    def __str__(self):
        return self.id
    
    
