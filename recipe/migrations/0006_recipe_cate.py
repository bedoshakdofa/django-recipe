# Generated by Django 3.2.18 on 2023-04-27 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_auto_20230427_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cate',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='recipe.catagory'),
        ),
    ]
