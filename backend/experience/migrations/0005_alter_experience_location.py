# Generated by Django 4.2.4 on 2024-02-14 18:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("experience", "0004_alter_experience_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="experience",
            name="location",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]