# Generated by Django 2.0.2 on 2018-03-19 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facer', '0008_settings_quagga_seq'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machines',
            name='ssh',
        ),
    ]