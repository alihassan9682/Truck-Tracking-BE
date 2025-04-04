# Generated by Django 4.2.20 on 2025-03-27 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=12345, max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='fname',
            field=models.CharField(default=12345, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='lname',
            field=models.CharField(default=12345, max_length=20),
            preserve_default=False,
        ),
    ]
