# Generated by Django 5.0 on 2024-02-01 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_course_program'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='department',
            field=models.CharField(choices=[('CSE(R)', 'CSE(REGULAR)'), ('CSE(H)', 'CSE(HONORS)'), ('CSIT', 'CS&IT'), ('MECH', 'MECHANICAL'), ('civil', 'CIVIL'), ('ECE', 'ECE')], max_length=100),
        ),
    ]
