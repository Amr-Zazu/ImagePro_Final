# Generated by Django 3.1.7 on 2021-07-02 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images_api', '0010_auto_20210702_1300'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ImageField',
            new_name='ImageName',
        ),
    ]
