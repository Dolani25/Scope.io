# Generated by Django 4.1 on 2024-07-19 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_airdrop_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airdrop',
            name='slug',
            field=models.SlugField(blank=True, default=1721398103, null=True, unique=True),
        ),
    ]
