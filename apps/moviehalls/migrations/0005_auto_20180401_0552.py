# Generated by Django 2.0.3 on 2018-04-01 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviehalls', '0004_reserved_seat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviescurrentlyshowing',
            name='black_hall_movies',
        ),
        migrations.RemoveField(
            model_name='moviescurrentlyshowing',
            name='blue_hall_movies',
        ),
        migrations.RemoveField(
            model_name='moviescurrentlyshowing',
            name='red_hall_movies',
        ),
        migrations.AlterField(
            model_name='reserved',
            name='seat',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='MoviesCurrentlyShowing',
        ),
    ]
