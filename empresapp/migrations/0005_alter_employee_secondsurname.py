# Generated by Django 5.0.1 on 2024-02-19 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresapp', '0004_alter_employee_dismissaldate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='SecondSurname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
