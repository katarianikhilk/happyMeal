# Generated by Django 2.2.10 on 2020-07-22 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20200721_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='chef_key',
            field=models.CharField(default='22-Jul-2020 (09:31:25.080979)', max_length=100),
        ),
    ]