# Generated by Django 5.0.7 on 2024-11-24 21:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nejlepsiProjekt', '0008_rename_content_partner_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='unique_features', to='nejlepsiProjekt.partner'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='icon',
            field=models.CharField(help_text='Třída ikony FontAwesome nebo jiné knihovny', max_length=255),
        ),
        migrations.AlterField(
            model_name='feature',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]