# Generated by Django 2.2.10 on 2020-07-18 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20200718_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='chef_key',
            field=models.CharField(default='18-Jul-2020 (14:20:16.456100)', max_length=100),
        ),
    ]
