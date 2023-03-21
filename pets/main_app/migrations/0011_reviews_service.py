# Generated by Django 4.1.7 on 2023-03-21 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_remove_service_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='service',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.service'),
            preserve_default=False,
        ),
    ]