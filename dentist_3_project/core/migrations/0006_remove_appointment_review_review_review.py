# Generated by Django 4.0.3 on 2022-04-03 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_appointment_appointment_appointment_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='review',
        ),
        migrations.AddField(
            model_name='review',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.appointment'),
        ),
    ]
