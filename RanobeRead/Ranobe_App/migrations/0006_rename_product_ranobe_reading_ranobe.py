# Generated by Django 3.2.3 on 2021-05-24 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ranobe_App', '0005_delete_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ranobe_reading',
            old_name='product',
            new_name='ranobe',
        ),
    ]
