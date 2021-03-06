# Generated by Django 2.0.7 on 2018-07-21 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.IntegerField(default=False)),
                ('cookie', models.TextField(default=None, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'accounts',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='acounts',
            name='website',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Website'),
        ),
    ]
