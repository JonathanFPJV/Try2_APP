# Generated by Django 5.1.2 on 2024-10-15 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_rfid', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rfid',
            name='id_esp32',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='rfid',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
