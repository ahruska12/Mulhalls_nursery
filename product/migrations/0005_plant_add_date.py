# Generated by Django 4.2.10 on 2024-05-06 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_annual_annual_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='add_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]