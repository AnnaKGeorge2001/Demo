# Generated by Django 4.2.5 on 2023-09-30 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_alter_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2001-12-06'),
            preserve_default=False,
        ),
    ]
