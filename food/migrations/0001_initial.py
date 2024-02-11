# Generated by Django 4.2.1 on 2024-01-28 07:55

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Food",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("food_category_id", models.IntegerField(default=0)),
                ("calorie", models.FloatField(blank=True, null=True)),
                ("protein", models.FloatField(blank=True, null=True)),
                ("fat", models.FloatField(blank=True, null=True)),
                ("carbohydrates", models.FloatField(blank=True, null=True)),
                ("delete_flg", models.BooleanField(default=False)),
                ("created_datetime", models.DateTimeField(auto_now_add=True)),
                ("updated_datetime", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "food",
            },
        ),
        migrations.CreateModel(
            name="FoodCategory",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("category", models.IntegerField(default=0)),
                ("delete_flg", models.BooleanField(default=False)),
                ("created_datetime", models.DateTimeField(auto_now_add=True)),
                ("updated_datetime", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "food_category",
            },
        ),
    ]