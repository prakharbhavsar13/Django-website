# Generated by Django 3.0.5 on 2020-04-16 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carbike', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
