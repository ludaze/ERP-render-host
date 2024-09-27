# Generated by Django 5.0 on 2024-02-09 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmic', '0015_purchase_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='cosmic_purchase',
            name='remaining',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchase_item',
            name='remaining',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchase_item',
            name='purchase_no',
            field=models.ForeignKey(blank=True, db_column='purchase_no', null=True, on_delete=django.db.models.deletion.CASCADE, to='cosmic.cosmic_purchase'),
        ),
    ]
