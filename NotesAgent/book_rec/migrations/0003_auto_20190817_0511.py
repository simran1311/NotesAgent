# Generated by Django 2.2.4 on 2019-08-17 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_rec', '0002_auto_20190816_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrecd',
            name='book_p',
            field=models.FileField(upload_to=''),
        ),
    ]
