# Generated by Django 3.2.18 on 2023-04-27 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_auto_20230427_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagory', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='recipe_category',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='puplished',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
