# Generated by Django 4.1 on 2022-09-06 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0005_alter_tasks_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
