# Generated by Django 5.2.4 on 2025-07-16 05:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('contact_person', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subdivision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.developer')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('region', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('city_or_municipality', models.CharField(max_length=100)),
                ('barangay', models.CharField(blank=True, max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('lot_area_sqm', models.DecimalField(decimal_places=2, max_digits=10)),
                ('floor_area_sqm', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('status', models.CharField(choices=[('available', 'Available'), ('reserved', 'Reserved'), ('sold', 'Sold')], default='available', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('developer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='properties.developer')),
                ('subdivision', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='properties.subdivision')),
            ],
        ),
    ]
