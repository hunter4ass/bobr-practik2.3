# Generated by Django 5.1.2 on 2024-10-26 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
