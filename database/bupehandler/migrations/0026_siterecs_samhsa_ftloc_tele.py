# Generated by Django 3.1.7 on 2021-03-22 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bupehandler', '0025_auto_20210318_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='siterecs_samhsa_ftloc',
            name='tele',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
