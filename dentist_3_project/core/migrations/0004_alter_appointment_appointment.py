# Generated by Django 4.0.3 on 2022-04-03 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_review_appointment_appointment_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointment', to='core.review'),
        ),
    ]
