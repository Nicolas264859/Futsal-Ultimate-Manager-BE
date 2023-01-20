# Generated by Django 4.1.3 on 2023-01-18 20:04

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('futsal_sim', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matchresult',
            name='cpu_average_skill',
        ),
        migrations.RemoveField(
            model_name='matchresult',
            name='cpu_team_name',
        ),
        migrations.AddField(
            model_name='matchresult',
            name='coin_reward',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='matchresult',
            name='cpu_team',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cpu_team', to='futsal_sim.team'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='matchresult',
            name='player_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_team', to='futsal_sim.team'),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=32, validators=[django.core.validators.MaxLengthValidator(32), django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AlterField(
            model_name='team',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teams', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='teamsheet',
            name='goalkeeper',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='goalkeeper_%(class)s', to='futsal_sim.player'),
        ),
        migrations.AlterField(
            model_name='teamsheet',
            name='left_attacker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='left_attacker_%(class)s', to='futsal_sim.player'),
        ),
        migrations.AlterField(
            model_name='teamsheet',
            name='left_defender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='left_defender_%(class)s', to='futsal_sim.player'),
        ),
        migrations.AlterField(
            model_name='teamsheet',
            name='right_attacker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='right_attacker_%(class)s', to='futsal_sim.player'),
        ),
        migrations.AlterField(
            model_name='teamsheet',
            name='right_defender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='right_defender_%(class)s', to='futsal_sim.player'),
        ),
        migrations.CreateModel(
            name='TeamLineup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('goalkeeper', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='goalkeeper_%(class)s', to='futsal_sim.player')),
                ('left_attacker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='left_attacker_%(class)s', to='futsal_sim.player')),
                ('left_defender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='left_defender_%(class)s', to='futsal_sim.player')),
                ('right_attacker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='right_attacker_%(class)s', to='futsal_sim.player')),
                ('right_defender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='right_defender_%(class)s', to='futsal_sim.player')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='futsal_sim.team')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlayerMatchMoment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('minute', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(40)])),
                ('moment_type', models.CharField(choices=[('assist', 'Assist'), ('goal', 'Goal')], max_length=32)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_moments', to='futsal_sim.matchresult')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_moments', to='futsal_sim.player')),
            ],
        ),
        migrations.AddField(
            model_name='matchresult',
            name='cpu_lineup',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='matches_as_cpu', to='futsal_sim.teamlineup'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='matchresult',
            name='player_lineup',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='matches_as_player', to='futsal_sim.teamlineup'),
            preserve_default=False,
        ),
        migrations.AddConstraint(
            model_name='playermatchmoment',
            constraint=models.CheckConstraint(check=models.Q(('moment_type__in', ['assist', 'goal'])), name='futsal_sim_playermatchmoment_moment_type_valid'),
        ),
    ]