# Generated by Django 3.0.3 on 2020-04-22 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HKJC_database', '0012_trainer_report_trainer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jockey_report',
            name='jockey',
        ),
        migrations.DeleteModel(
            name='Jockey_Info',
        ),
        migrations.DeleteModel(
            name='Jockey_Report',
        ),
    ]
