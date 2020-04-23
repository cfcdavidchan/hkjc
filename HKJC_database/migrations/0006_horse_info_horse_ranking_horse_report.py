# Generated by Django 3.0.3 on 2020-04-23 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HKJC_database', '0005_auto_20200424_0538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horse_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter the horse's name", max_length=50)),
                ('chinese_name', models.CharField(blank=True, help_text="Enter the horse's chinese name", max_length=50)),
                ('hkjc_id', models.CharField(help_text="Enter the horse's hkjc id", max_length=20)),
                ('origin', models.CharField(help_text="Enter the horse's origin", max_length=50)),
                ('age', models.IntegerField(help_text="Enter the horse's age")),
                ('owner', models.CharField(help_text="Enter the horse's owner", max_length=100)),
                ('sire', models.CharField(help_text="Enter the horse's sire", max_length=100)),
                ('dam', models.CharField(help_text="Enter the horse's dam", max_length=100)),
                ('dam_sire', models.CharField(blank=True, help_text="Enter the horse's dam_sire", max_length=100)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('trainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='horse_info_trainer', to='HKJC_database.Trainer_Info')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Horse_Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_rank', models.IntegerField(help_text="Enter the horse's current_rank")),
                ('season_start_rank', models.IntegerField(help_text="Enter the horse's starting rank of this season")),
                ('season_stakes', models.FloatField(help_text="Enter the horse's season stakes")),
                ('total_stakes', models.FloatField(help_text="Enter the horse's total stakes")),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('horse', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='horse_info_horse', to='HKJC_database.Horse_Info')),
            ],
            options={
                'ordering': ['horse'],
            },
        ),
        migrations.CreateModel(
            name='Horse_Ranking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(help_text="Enter the horse's rank")),
                ('rank_reord_date', models.DateField(help_text='Enter the record date of the rank')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('horse', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='horse_ranking_horse', to='HKJC_database.Horse_Info')),
            ],
            options={
                'ordering': ['horse'],
            },
        ),
    ]
