# Generated by Django 4.2 on 2023-04-16 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='status',
            field=models.CharField(default='pending', max_length=100),
        ),
    ]
