# Generated by Django 5.0.1 on 2024-02-23 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='display_name',
            field=models.CharField(default='user_default_name', max_length=250),
            preserve_default=False,
        ),
    ]