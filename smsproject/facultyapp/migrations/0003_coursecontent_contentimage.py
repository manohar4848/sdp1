# Generated by Django 5.0 on 2024-03-04 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultyapp', '0002_remove_coursecontent_contentimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursecontent',
            name='contentimage',
            field=models.FileField(default=0, upload_to='coursecontent'),
            preserve_default=False,
        ),
    ]
