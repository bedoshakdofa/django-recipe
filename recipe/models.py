from django.db import models
from django.contrib.auth.models import User

class catagory(models.Model):
    catagory=models.CharField(max_length=20)
    
    def __str__(self):
        return self.catagory


class recipe(models.Model):

    option=[
        ('puplished','puplished'),
        ('draft','draft')
    ]
    recipe_name=models.CharField(max_length=20)
    recipe_ingred=models.TextField(null=True)
    img=models.ImageField(upload_to='photo/%y/%m/%d')
    recipe_step=models.TextField(max_length=2000)
    status=models.CharField(max_length=20,choices=option)
    puplished=models.DateTimeField(auto_now=True)
    auther=models.ForeignKey(User,on_delete=models.CASCADE)
    cate=models.ForeignKey(catagory,on_delete=models.CASCADE)

    def __str__(self):
        return self.recipe_name

