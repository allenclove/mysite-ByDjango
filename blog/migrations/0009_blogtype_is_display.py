# Generated by Django 2.0 on 2019-07-08 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180723_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogtype',
            name='is_display',
            field=models.BooleanField(default=True),
        ),
    ]
