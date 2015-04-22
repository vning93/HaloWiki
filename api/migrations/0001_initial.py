# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('criteria', models.CharField(default=b'', max_length=200, null=True, blank=True)),
                ('emblem', models.CharField(default=b'', max_length=30, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Achievement_Unlockable_In_Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('achievement', models.ForeignKey(to='api.Achievement')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('current_status', models.CharField(default=b'', max_length=200, null=True, blank=True)),
                ('home_world', models.CharField(default=b'', max_length=50, null=True, blank=True)),
                ('gender', models.CharField(max_length=10, choices=[(b'MALE', b'Male'), (b'FEMALE', b'Female')])),
                ('birth_date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Character_Appear_In_Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('character', models.ForeignKey(to='api.Character')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('year', models.DateField()),
                ('developer', models.CharField(default=b'', max_length=50, null=True, blank=True)),
                ('publisher', models.CharField(default=b'', max_length=50, null=True, blank=True)),
                ('rating', models.DecimalField(max_digits=6, decimal_places=2)),
                ('platform', models.CharField(default=b'', max_length=50, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Game_Mode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('multi_player', models.BooleanField(default=False)),
                ('emblem', models.CharField(default=b'', max_length=30, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Game_Mode_Playable_On_Map',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('game_mode', models.ForeignKey(to='api.Game_Mode')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Game_Playable_Game_Mode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('game', models.ForeignKey(to='api.Game')),
                ('game_mode', models.ForeignKey(to='api.Game_Mode')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('location', models.CharField(default=b'', max_length=200, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('model', models.CharField(default=b'', max_length=50, null=True, blank=True)),
                ('_class', models.CharField(default=b'', max_length=25, null=True, blank=True)),
                ('num_users', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vehicle_Usable_On_Map',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('map', models.ForeignKey(to='api.Map')),
                ('vehicle', models.ForeignKey(to='api.Vehicle')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('firing_mode', models.CharField(max_length=10, choices=[(b'SEMI', b'Semi'), (b'AUTOMATIC', b'Automatic'), (b'MELEE', b'Melee')])),
                ('damage_level', models.DecimalField(max_digits=8, decimal_places=2)),
                ('dual_wield', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Weapon_Usable_On_Map',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('map', models.ForeignKey(to='api.Map')),
                ('weapon', models.ForeignKey(to='api.Weapon')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='game_mode_playable_on_map',
            name='map',
            field=models.ForeignKey(to='api.Map'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='api.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character_appear_in_game',
            name='game',
            field=models.ForeignKey(to='api.Game'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='achievement_unlockable_in_game',
            name='game',
            field=models.ForeignKey(to='api.Game'),
            preserve_default=True,
        ),
    ]
