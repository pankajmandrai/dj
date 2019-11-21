# Generated by Django 2.0.7 on 2018-11-20 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('idno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('clas', models.IntegerField()),
                ('total', models.IntegerField()),
                ('average', models.DecimalField(decimal_places=2, max_digits=5)),
                ('grade', models.CharField(max_length=2)),
            ],
        ),
    ]