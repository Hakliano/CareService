# Generated by Django 5.0.7 on 2024-11-24 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nejlepsiProjekt', '0010_remove_feature_partner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='icon',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='feature',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]