# Generated by Django 3.2.3 on 2021-05-24 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ranobe_App', '0003_auto_20210524_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ranobe_reading',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(max_length=50),
        ),
    ]
