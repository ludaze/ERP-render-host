# Generated by Django 5.0 on 2023-12-14 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer_profile',
            fields=[
                ('customer_name', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('customer_address', models.TextField(blank=True)),
                ('contact_person', models.TextField(blank=True)),
                ('phone_number', models.CharField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
