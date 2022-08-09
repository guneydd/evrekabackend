# Generated by Django 4.1 on 2022-08-09 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evrekabackend', '0004_bin_collection_operation'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='bin',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='evrekabackend.bin'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collection',
            name='operation',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='evrekabackend.operation'),
            preserve_default=False,
        ),
    ]