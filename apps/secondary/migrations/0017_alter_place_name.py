# Generated by Django 5.0 on 2023-12-23 16:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0016_alter_reach_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='name',
            field=ckeditor.fields.RichTextField(verbose_name='Название'),
        ),
    ]