# Generated by Django 2.0.7 on 2018-07-22 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180722_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='acounts',
            name='ip',
            field=models.CharField(blank=True, max_length=125, null=True),
        ),
    ]