# Generated by Django 2.0.9 on 2019-01-30 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='order_topic',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_files',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
