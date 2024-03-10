# Generated by Django 5.0 on 2024-02-28 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0012_facultycoursemapping'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='credits',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='ltps',
            field=models.CharField(default='0-0-0-0', max_length=10),
            preserve_default=False,
        ),
    ]