# Generated by Django 2.2.10 on 2020-07-21 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20200720_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='chef_key',
            field=models.CharField(default='21-Jul-2020 (14:54:25.810662)', max_length=100),
        ),
    ]