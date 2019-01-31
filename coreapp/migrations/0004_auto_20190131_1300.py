# Generated by Django 2.0.10 on 2019-01-31 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_available', models.BooleanField(default=False)),
                ('is_pending', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=False)),
                ('is_editing', models.BooleanField(default=False)),
                ('is_paid', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='is_approved',
        ),
        migrations.RemoveField(
            model_name='order',
            name='is_available',
        ),
        migrations.RemoveField(
            model_name='order',
            name='is_editing',
        ),
        migrations.RemoveField(
            model_name='order',
            name='is_paid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='is_pending',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='coreapp.Status'),
        ),
    ]
