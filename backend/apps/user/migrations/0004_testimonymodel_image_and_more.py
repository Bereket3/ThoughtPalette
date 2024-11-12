# Generated by Django 5.0 on 2024-07-01 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_testimonymodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonymodel',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='testimony_pictures/'),
        ),
        migrations.AlterField(
            model_name='authusermodel',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]