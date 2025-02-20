# Generated by Django 5.1.4 on 2025-01-11 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=255)),
                ('available_for', models.CharField(max_length=50)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('per_sq_feet_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('property_type', models.CharField(max_length=50)),
                ('bedroom', models.IntegerField()),
                ('bathroom', models.IntegerField()),
                ('parking', models.IntegerField()),
                ('area', models.DecimalField(decimal_places=2, max_digits=10)),
                ('year', models.IntegerField()),
                ('address', models.TextField()),
                ('details', models.TextField()),
            ],
        ),
    ]
