# Generated by Django 2.2.5 on 2019-09-29 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_auto_20190929_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='time_to_remind',
            field=models.PositiveIntegerField(choices=[(1, 'За час'), (2, 'За 2 часа'), (4, 'За 4 часа'), (24, 'За день'), (168, 'За неделю')]),
        ),
    ]