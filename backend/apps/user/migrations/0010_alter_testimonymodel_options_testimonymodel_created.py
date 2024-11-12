# Generated by Django 5.0 on 2024-08-01 17:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_remove_testimonymodel_image_testimonymodel_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testimonymodel',
            options={'ordering': ('-created', 'approved')},
        ),
        migrations.AddField(
            model_name='testimonymodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
