# Generated by Django 4.1 on 2024-07-19 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_airdrop_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airdrop',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
