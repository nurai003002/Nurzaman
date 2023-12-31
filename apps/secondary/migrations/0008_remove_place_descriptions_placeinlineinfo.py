# Generated by Django 5.0 on 2023-12-21 11:31

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0007_place'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='descriptions',
        ),
        migrations.CreateModel(
            name='PlaceInlineInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptions', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Информационный текст')),
                ('place_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_inline_info', to='secondary.place')),
            ],
            options={
                'unique_together': {('place_info', 'descriptions')},
            },
        ),
    ]
