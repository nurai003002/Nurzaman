# Generated by Django 5.0 on 2023-12-23 17:11

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_settingsplace'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='box_office',
            field=ckeditor.fields.RichTextField(default=1, verbose_name='Офис продажи'),
            preserve_default=False,
        ),
    ]
