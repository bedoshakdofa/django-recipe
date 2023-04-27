from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class recipe(models.Model):
    x=[
        ('dessert','dessert'),
        ('chicken','Chicken'),
        ('meat','Meat'),
        ('drinks','drinks'),
    ]

    option=[
        ('puplished','puplished'),
        ('draft','draft')
    ]
    recipe_name=models.CharField(max_length=20)
    recipe_ingred=models.TextField(null=True)
    img=models.ImageField(upload_to='photo/%y/%m/%d',default=1)
    recipe_step=models.TextField(max_length=2000,default=1)
    recipe_category=models.CharField(max_length=30,null=False,choices=x,default=1)
    status=models.CharField(max_length=20,choices=option,default=1)
    puplished=models.DateTimeField(default=timezone.now )
    auther=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.id

