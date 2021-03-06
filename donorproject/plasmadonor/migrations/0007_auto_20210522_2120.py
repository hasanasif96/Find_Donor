# Generated by Django 3.1.7 on 2021-05-22 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plasmadonor', '0006_auto_20210519_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='slug',
        ),
        migrations.AddField(
            model_name='donor',
            name='Blood_Group',
            field=models.CharField(choices=[("Don't know", "Don't know"), ('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], default="Don't know", max_length=50),
        ),
        migrations.AddField(
            model_name='donor',
            name='age',
            field=models.CharField(default='10', max_length=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='donor',
            name='description',
            field=models.CharField(max_length=80),
        ),
                
        migrations.AlterField(
            model_name='requests',
            name='currrent_situation',
            field=models.CharField(choices=[('Very Serious', 'Very Serious'), ('In Ventilator', 'In Ventilator'), ('Oxygen Below 50', 'Oxygen Below 50'), ('Not so serious', 'Not so serious')], max_length=40),
        ),
    ]
