# Generated by Django 3.2.16 on 2023-12-10 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0016_auto_20231130_0907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='classroom',
        ),
    ]
