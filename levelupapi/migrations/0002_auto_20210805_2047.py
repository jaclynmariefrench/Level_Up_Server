# Generated by Django 3.2.6 on 2021-08-05 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='attendees',
        ),
        migrations.AddField(
            model_name='game',
            name='skill_level',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]