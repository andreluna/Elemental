# Generated by Django 2.2.6 on 2019-12-09 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('data_source', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'data source',
                'verbose_name_plural': 'data sources',
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('platform_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'platform',
                'verbose_name_plural': 'platforms',
            },
        ),
        migrations.CreateModel(
            name='Tactic',
            fields=[
                ('tactic_id', models.CharField(max_length=10)),
                ('tactic_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('tactic_description', models.TextField()),
                ('tactic_url', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'tactic',
                'verbose_name_plural': 'tactics',
            },
        ),
        migrations.CreateModel(
            name='Technique',
            fields=[
                ('technique_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('technique_name', models.CharField(max_length=40)),
                ('technique_description', models.TextField()),
                ('technique_detection', models.TextField()),
                ('technique_url', models.CharField(max_length=200)),
                ('technique_abbreviation', models.CharField(blank=True, max_length=4, null=True)),
                ('created', models.DateField(blank=True, null=True)),
                ('modified', models.DateField(blank=True, null=True)),
                ('atomic_yml', models.FileField(blank=True, null=True, upload_to='atomics/')),
                ('atomic_md', models.FileField(blank=True, null=True, upload_to='atomics/')),
                ('data_source', models.ManyToManyField(to='matrix.DataSource')),
                ('platform', models.ManyToManyField(to='matrix.Platform')),
                ('tactic_name', models.ManyToManyField(to='matrix.Tactic')),
            ],
            options={
                'verbose_name': 'technique',
                'verbose_name_plural': 'techniques',
            },
        ),
        migrations.CreateModel(
            name='SigmaRule',
            fields=[
                ('rule_file', models.FileField(upload_to='sigma_rules/')),
                ('rule_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('detection_created', models.BooleanField(blank=True, null=True)),
                ('technique', models.ManyToManyField(to='matrix.Technique')),
            ],
            options={
                'verbose_name': 'sigma rule',
                'verbose_name_plural': 'sigma rules',
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('date', models.DateField(blank=True, null=True)),
                ('technique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='matrix.Technique')),
            ],
            options={
                'verbose_name': 'note',
                'verbose_name_plural': 'notes',
            },
        ),
        migrations.CreateModel(
            name='LogSource',
            fields=[
                ('log_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('data_source', models.ManyToManyField(to='matrix.DataSource')),
                ('platform', models.ManyToManyField(to='matrix.Platform')),
            ],
            options={
                'verbose_name': 'log source',
                'verbose_name_plural': 'log sources',
            },
        ),
    ]
