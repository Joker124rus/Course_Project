# Generated by Django 3.2.3 on 2021-05-25 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ranobe_App', '0007_ranobe_reading_chapternumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ranobe_reading',
            name='chapterNumber',
            field=models.IntegerField(),
        ),
    ]