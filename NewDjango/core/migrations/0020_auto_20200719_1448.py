# Generated by Django 2.2.10 on 2020-07-19 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20200718_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='chef_key',
            field=models.CharField(default='19-Jul-2020 (14:48:23.055626)', max_length=100),
        ),
    ]
