# Generated by Django 5.0.7 on 2024-07-21 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0002_alter_task_date_of_creation_alter_task_deadline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='photo',
        ),
        migrations.AddField(
            model_name='autor',
            name='surname',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]