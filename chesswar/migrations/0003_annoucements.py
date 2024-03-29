# Generated by Django 5.0.2 on 2024-02-09 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chesswar', '0002_alter_duel_arbiter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annoucements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('warning_alert', models.BooleanField(default=True)),
                ('danger_alert', models.BooleanField(default=False)),
                ('success_alert', models.BooleanField(default=False)),
            ],
        ),
    ]
