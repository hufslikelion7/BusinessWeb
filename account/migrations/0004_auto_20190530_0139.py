# Generated by Django 2.1.5 on 2019-05-29 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_users_user_password2'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='cehck_num',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='check_pass',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]