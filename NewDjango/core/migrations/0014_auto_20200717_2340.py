# Generated by Django 2.2.10 on 2020-07-17 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0013_orderitem_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='chef_key',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('O', 'Order Request Accepted'), ('C', 'Cooking'), ('D', 'Deliverd')], default='O', max_length=1),
        ),
        migrations.CreateModel(
            name='OrderedList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('orderitems', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.OrderItem')),
            ],
        ),
    ]
