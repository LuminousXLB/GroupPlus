# Generated by Django 3.2.7 on 2021-09-17 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='desc',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='number',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
