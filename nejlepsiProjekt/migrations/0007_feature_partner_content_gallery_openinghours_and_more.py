# Generated by Django 5.0.7 on 2024-11-24 01:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nejlepsiProjekt', '0006_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='partner',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='partner_gallery/')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='nejlepsiProjekt.partner')),
            ],
        ),
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Monday', 'Pondělí'), ('Tuesday', 'Úterý'), ('Wednesday', 'Středa'), ('Thursday', 'Čtvrtek'), ('Friday', 'Pátek'), ('Saturday', 'Sobota'), ('Sunday', 'Neděle')], max_length=10)),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opening_hours', to='nejlepsiProjekt.partner')),
            ],
        ),
        migrations.CreateModel(
            name='PartnerFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nejlepsiProjekt.feature')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='nejlepsiProjekt.partner')),
            ],
        ),
        migrations.CreateModel(
            name='PriceList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price_list', to='nejlepsiProjekt.partner')),
            ],
        ),
    ]