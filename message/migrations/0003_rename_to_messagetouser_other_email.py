# Generated by Django 4.0.1 on 2022-01-31 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_messagetouser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messagetouser',
            old_name='to',
            new_name='other_email',
        ),
    ]