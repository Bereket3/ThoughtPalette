# Generated by Django 5.0 on 2024-07-05 15:54

import user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('user', '0004_testimonymodel_image_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='authusermodel',
            managers=[
                ('objects', user.models.AuthUserAccountManager()),
            ],
        ),
        migrations.AlterField(
            model_name='authusermodel',
            name='groups',
            field=models.ManyToManyField(blank=True, default=None, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='authusermodel',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='authusermodel',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AlterField(
            model_name='authusermodel',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, default=None, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
