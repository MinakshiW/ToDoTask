# Generated by Django 5.0.7 on 2024-08-01 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_task_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
