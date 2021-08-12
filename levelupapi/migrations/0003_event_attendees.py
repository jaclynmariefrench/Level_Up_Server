# Generated by Django 3.2.6 on 2021-08-12 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0002_auto_20210805_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(related_name='attending', through='levelupapi.EventGamer', to='levelupapi.Gamer'),
        ),
    ]
