# Generated by Django 3.0.3 on 2020-04-24 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HKJC_database', '0009_match_info_match_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match_result',
            name='horse',
        ),
        migrations.RemoveField(
            model_name='match_result',
            name='jockey',
        ),
        migrations.RemoveField(
            model_name='match_result',
            name='match',
        ),
        migrations.DeleteModel(
            name='Match_Info',
        ),
        migrations.DeleteModel(
            name='Match_Result',
        ),
    ]
