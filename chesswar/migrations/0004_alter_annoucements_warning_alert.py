# Generated by Django 5.0.2 on 2024-02-09 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chesswar', '0003_annoucements'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annoucements',
            name='warning_alert',
            field=models.BooleanField(default=False),
        ),
    ]