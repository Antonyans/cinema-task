# Generated by Django 2.0.3 on 2018-04-02 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviehalls', '0007_auto_20180402_0522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blackhall',
            name='hall_name',
        ),
        migrations.RemoveField(
            model_name='bluehall',
            name='hall_name',
        ),
        migrations.RemoveField(
            model_name='redhall',
            name='hall_name',
        ),
    ]