# Generated by Django 4.0.3 on 2022-04-15 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_alter_service_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.CharField(choices=[('1', 'Preventative'), ('2', 'Restorative'), ('3', 'Cosmetic')], max_length=30),
        ),
    ]
