# Generated by Django 3.2.6 on 2021-08-27 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hw_7_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='craated_by',
            new_name='created_by',
        ),
    ]