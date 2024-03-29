# Generated by Django 5.0.2 on 2024-02-12 22:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0002_rename_user_id_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('education_id', models.AutoField(primary_key=True, serialize=False)),
                ('institution_name', models.CharField(max_length=100)),
                ('field', models.CharField(blank=True, max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('start_year', models.IntegerField()),
                ('end_year', models.IntegerField()),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.employee')),
            ],
        ),
    ]
