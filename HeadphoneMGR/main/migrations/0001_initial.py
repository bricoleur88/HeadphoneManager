# Generated by Django 2.2.4 on 2020-04-13 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeadphoneMain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hp_model', models.CharField(max_length=100)),
                ('hp_serial', models.CharField(max_length=100)),
                ('hp_pDate', models.DateField()),
                ('hp_pDetail', models.TextField()),
                ('hp_rDate', models.DateField()),
                ('hp_rDetail', models.TextField()),
                ('hp_receiver', models.CharField(max_length=100)),
                ('hp_checker', models.CharField(max_length=100)),
                ('hp_state', models.CharField(max_length=100)),
            ],
        ),
    ]
