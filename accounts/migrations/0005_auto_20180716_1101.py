# Generated by Django 2.0.7 on 2018-07-16 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180716_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acounts',
            name='cookie',
            field=models.TextField(default=None, null=True),
        ),
    ]
