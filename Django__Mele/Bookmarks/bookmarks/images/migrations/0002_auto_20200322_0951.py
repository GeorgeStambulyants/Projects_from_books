# Generated by Django 3.0.4 on 2020-03-22 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='descriprion',
            new_name='description',
        ),
    ]
