# Generated by Django 4.1.4 on 2023-01-20 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-complete']},
        ),
    ]
