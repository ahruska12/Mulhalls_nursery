# Generated by Django 4.2.10 on 2024-04-16 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_rename_email_customer_customer_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionsasked',
            name='answer_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]