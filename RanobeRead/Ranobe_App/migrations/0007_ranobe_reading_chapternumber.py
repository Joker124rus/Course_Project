# Generated by Django 3.2.3 on 2021-05-24 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ranobe_App', '0006_rename_product_ranobe_reading_ranobe'),
    ]

    operations = [
        migrations.AddField(
            model_name='ranobe_reading',
            name='chapterNumber',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
