# Generated by Django 5.0 on 2024-02-20 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0007_alter_student_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/review_images/'),
        ),
    ]
