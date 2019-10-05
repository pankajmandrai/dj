# Generated by Django 2.2.1 on 2019-10-01 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guideline', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdata',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='patientdata',
            name='diastolic_BP',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='patientdata',
            name='fasting_blood_sugar',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='patientdata',
            name='no_of_packs',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='patientdata',
            name='obese',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='patientdata',
            name='smoking_years',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='patientdata',
            name='systolic_BP',
            field=models.PositiveIntegerField(default=0),
        ),
    ]