# Generated by Django 3.0.7 on 2020-07-13 06:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_models_member_product_material_storage'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='material',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
