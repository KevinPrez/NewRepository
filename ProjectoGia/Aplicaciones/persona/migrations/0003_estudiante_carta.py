# Generated by Django 4.0.4 on 2022-04-19 16:28

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_alter_estudiante_options_alter_estudiante_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='carta',
            field=ckeditor.fields.RichTextField(default='Vamos!!!'),
            preserve_default=False,
        ),
    ]
