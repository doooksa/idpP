# Generated by Django 2.0.13 on 2022-04-25 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20220425_2107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='title',
            new_name='name',
        ),
    ]