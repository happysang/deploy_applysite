# Generated by Django 3.0.8 on 2020-08-06 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200806_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='manager_ok',
            field=models.BooleanField(null=True),
        ),
    ]
