# Generated by Django 5.0.7 on 2024-07-18 14:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('branches', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.city')),
            ],
        ),
        migrations.CreateModel(
            name='resturanttype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.city')),
            ],
        ),
        migrations.CreateModel(
            name='places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.city')),
                ('resturant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.resturanttype')),
            ],
        ),
        migrations.CreateModel(
            name='foodtype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('type', models.CharField(max_length=100)),
                ('resurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.resturanttype')),
            ],
        ),
        migrations.CreateModel(
            name='food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('resturant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.resturanttype')),
            ],
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.city')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.foodtype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.profile')),
                ('resturant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.resturanttype')),
            ],
        ),
    ]
