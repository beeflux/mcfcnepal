# Generated by Django 2.2.2 on 2019-06-29 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0009_adminmember'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminmember',
            name='position',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterModelTable(
            name='members',
            table='Member',
        ),
    ]
