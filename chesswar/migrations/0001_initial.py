# Generated by Django 4.1.6 on 2023-07-20 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boardno', models.IntegerField(default=0, verbose_name='Board Number')),
                ('location', models.CharField(blank=True, max_length=100, null=True, verbose_name='Board Location')),
                ('busy', models.BooleanField(default=False, verbose_name='Match Live On Board?')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Participant Name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Participant Email')),
                ('phone', models.CharField(max_length=10, unique=True, verbose_name='Participant Contact')),
                ('level', models.IntegerField(default=1, verbose_name='Round Number Qualified For')),
                ('waiting', models.BooleanField(default=True, verbose_name='In Waiting?')),
                ('reg_time', models.DateTimeField(auto_now_add=True, verbose_name='Registration Time')),
                ('last_round', models.DateTimeField(auto_now=True, verbose_name='Time Of Last Round Played')),
            ],
        ),
        migrations.CreateModel(
            name='Duel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arbiter', models.CharField(blank=True, max_length=40, null=True)),
                ('level', models.IntegerField(default=1)),
                ('start', models.DateTimeField(auto_now_add=True, verbose_name='Starting Time')),
                ('over', models.BooleanField(default=False, verbose_name='Duel Over?')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='chesswar.board', verbose_name='Board Number')),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='PlayerWhitePiece', to='chesswar.registration', verbose_name='Player-White-Piece')),
                ('player2', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='PlayerBlackPiece', to='chesswar.registration', verbose_name='Player-Black-Piece')),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='BoardWinner', to='chesswar.registration', verbose_name='Board Winner')),
            ],
        ),
    ]
