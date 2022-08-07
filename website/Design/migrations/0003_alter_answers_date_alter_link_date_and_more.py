# Generated by Django 4.0.4 on 2022-05-29 14:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Design', '0002_alter_answers_date_alter_link_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 29, 20, 12, 57, 528614)),
        ),
        migrations.AlterField(
            model_name='link',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 29, 20, 12, 57, 528614)),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 29, 20, 12, 57, 528614)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 29, 20, 12, 57, 528614)),
        ),
        migrations.AlterField(
            model_name='query',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 29, 20, 12, 57, 528614)),
        ),
        migrations.AlterField(
            model_name='questions',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 29, 20, 12, 57, 528614)),
        ),
        migrations.AlterField(
            model_name='register',
            name='authority',
            field=models.CharField(choices=[('hod', 'hod'), ('faculty', 'faculty'), ('student', 'student')], max_length=10),
        ),
        migrations.AlterField(
            model_name='register',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 5, 29, 20, 12, 57, 528614)),
        ),
    ]
