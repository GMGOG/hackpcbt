# Generated by Django 3.0.1 on 2019-12-29 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0002_auto_20191229_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='year',
            field=models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th')], max_length=6),
        ),
    ]
