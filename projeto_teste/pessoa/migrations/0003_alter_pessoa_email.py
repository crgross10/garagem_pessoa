# Generated by Django 3.2.5 on 2021-07-05 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0002_auto_20210703_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='email',
            field=models.EmailField(max_length=200, unique=True),
        ),
    ]
