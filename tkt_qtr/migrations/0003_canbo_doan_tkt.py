# Generated by Django 3.2.3 on 2021-10-11 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tkt_qtr', '0002_auto_20211011_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='canbo',
            name='doan_tkt',
            field=models.CharField(default='', max_length=20),
        ),
    ]
