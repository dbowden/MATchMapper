# Generated by Django 3.1.7 on 2021-07-24 20:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bupehandler', '0030_auto_20210719_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='siterecs_dbhids_tad',
            name='date_update',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='siterecs_dbhids_tad',
            name='latitude',
            field=models.FloatField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='siterecs_dbhids_tad',
            name='longitude',
            field=models.FloatField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='siterecs_hfp_fqhc',
            name='date_update',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='siterecs_hfp_fqhc',
            name='latitude',
            field=models.FloatField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='siterecs_hfp_fqhc',
            name='longitude',
            field=models.FloatField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='siterecs_other_srcs',
            name='map_marker',
            field=models.CharField(choices=[('ba_weekly', 'ba_weekly'), ('ba_monthly', 'ba_monthly'), ('dbhids_assessment', 'dbhids_assessment'), ('dbhids_coe', 'dbhids_coe'), ('dbhids_else', 'dbhids_else'), ('samhsa_otp', 'samhsa_otp'), ('samhsa_else', 'samhsa_else'), ('fqhc_else', 'fqhc_else'), ('other_mat', 'other_mat'), ('tbd_unclear', 'tbd_unclear'), ('xx_unlikely', 'xx_unlikely')], default='tbd_unclear', max_length=25),
        ),
        migrations.AddField(
            model_name='siterecs_samhsa_otp',
            name='latitude',
            field=models.FloatField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='siterecs_samhsa_otp',
            name='longitude',
            field=models.FloatField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sites_all',
            name='map_marker',
            field=models.CharField(choices=[('ba_weekly', 'ba_weekly'), ('ba_monthly', 'ba_monthly'), ('dbhids_assessment', 'dbhids_assessment'), ('dbhids_coe', 'dbhids_coe'), ('dbhids_else', 'dbhids_else'), ('samhsa_otp', 'samhsa_otp'), ('samhsa_else', 'samhsa_else'), ('fqhc_else', 'fqhc_else'), ('other_mat', 'other_mat'), ('tbd_unclear', 'tbd_unclear'), ('xx_unlikely', 'xx_unlikely')], default='tbd_unclear', max_length=25),
        ),
        migrations.AlterField(
            model_name='ba_dbhids_tad',
            name='why_hidden',
            field=models.CharField(blank=True, choices=[('No MAT?', 'No MAT?'), ('Site closed', 'Site closed'), ('Not a practice site', 'Not a practice site'), ('Record redundant', 'Record redundant'), ('Source removed record', 'Source removed record'), ('Too far from Philadelphia?', 'Too far from Philadelphia?'), ('Data needs review', 'Data needs review'), ('Other', 'Other')], max_length=150),
        ),
        migrations.AlterField(
            model_name='siterecs_dbhids_tad',
            name='why_hidden',
            field=models.CharField(blank=True, choices=[('No MAT?', 'No MAT?'), ('Site closed', 'Site closed'), ('Not a practice site', 'Not a practice site'), ('Record redundant', 'Record redundant'), ('Source removed record', 'Source removed record'), ('Too far from Philadelphia?', 'Too far from Philadelphia?'), ('Data needs review', 'Data needs review'), ('Other', 'Other')], max_length=150),
        ),
        migrations.AlterField(
            model_name='siterecs_hfp_fqhc',
            name='data_review',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='siterecs_hfp_fqhc',
            name='why_hidden',
            field=models.CharField(blank=True, choices=[('No MAT?', 'No MAT?'), ('Site closed', 'Site closed'), ('Not a practice site', 'Not a practice site'), ('Record redundant', 'Record redundant'), ('Source removed record', 'Source removed record'), ('Too far from Philadelphia?', 'Too far from Philadelphia?'), ('Data needs review', 'Data needs review'), ('Other', 'Other')], max_length=150),
        ),
        migrations.AlterField(
            model_name='siterecs_other_srcs',
            name='data_review',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='siterecs_other_srcs',
            name='why_hidden',
            field=models.CharField(blank=True, choices=[('No MAT?', 'No MAT?'), ('Site closed', 'Site closed'), ('Not a practice site', 'Not a practice site'), ('Record redundant', 'Record redundant'), ('Source removed record', 'Source removed record'), ('Too far from Philadelphia?', 'Too far from Philadelphia?'), ('Data needs review', 'Data needs review'), ('Other', 'Other')], max_length=150),
        ),
        migrations.AlterField(
            model_name='siterecs_samhsa_ftloc',
            name='why_hidden',
            field=models.CharField(blank=True, choices=[('No MAT?', 'No MAT?'), ('Site closed', 'Site closed'), ('Not a practice site', 'Not a practice site'), ('Record redundant', 'Record redundant'), ('Source removed record', 'Source removed record'), ('Too far from Philadelphia?', 'Too far from Philadelphia?'), ('Data needs review', 'Data needs review'), ('Other', 'Other')], max_length=150),
        ),
        migrations.AlterField(
            model_name='siterecs_samhsa_otp',
            name='why_hidden',
            field=models.CharField(blank=True, choices=[('No MAT?', 'No MAT?'), ('Site closed', 'Site closed'), ('Not a practice site', 'Not a practice site'), ('Record redundant', 'Record redundant'), ('Source removed record', 'Source removed record'), ('Too far from Philadelphia?', 'Too far from Philadelphia?'), ('Data needs review', 'Data needs review'), ('Other', 'Other')], max_length=150),
        ),
        migrations.AlterField(
            model_name='sites_all',
            name='data_review',
            field=models.CharField(blank=True, default=None, max_length=499),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sites_all',
            name='why_hidden',
            field=models.CharField(blank=True, choices=[('No MAT?', 'No MAT?'), ('Site closed', 'Site closed'), ('Not a practice site', 'Not a practice site'), ('Record redundant', 'Record redundant'), ('Source removed record', 'Source removed record'), ('Too far from Philadelphia?', 'Too far from Philadelphia?'), ('Data needs review', 'Data needs review'), ('Other', 'Other')], max_length=150),
        ),
    ]
