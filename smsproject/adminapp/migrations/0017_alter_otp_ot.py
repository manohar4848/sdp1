# Generated by Django 4.0.4 on 2024-03-09 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0016_alter_otp_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='ot',
            field=models.IntegerField(),
        ),
    ]
