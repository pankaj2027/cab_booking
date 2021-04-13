# Generated by Django 3.1.6 on 2021-04-13 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('driverdetail', '0002_auto_20210413_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver_registration',
            name='car_number',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='driver_registration',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='driver_registration',
            name='license_number',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='driver_registration',
            name='phone_number',
            field=models.BigIntegerField(unique=True),
        ),
        migrations.CreateModel(
            name='Driver_location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver', to='driverdetail.driver_registration')),
            ],
        ),
    ]