# Generated by Django 4.1.7 on 2023-04-02 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='c_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
