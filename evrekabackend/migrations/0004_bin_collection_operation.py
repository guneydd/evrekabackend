# Generated by Django 4.1 on 2022-08-09 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evrekabackend', '0003_alter_navigationrecord_datetime_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bin',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('frequency', models.IntegerField()),
                ('last_collection', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
