# Generated by Django 4.2.8 on 2023-12-05 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]