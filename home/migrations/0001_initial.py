# Generated by Django 4.2.2 on 2023-09-28 18:45

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('image_url_section_one', models.URLField(blank=True, max_length=1024, null=True)),
                ('content_section_one', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('icon', models.CharField(blank=True, max_length=200, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image_section_one', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
