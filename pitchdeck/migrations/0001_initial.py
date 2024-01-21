# Generated by Django 4.2.2 on 2023-09-28 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PitchDeck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('Sector', models.CharField(default=None, max_length=100)),
                ('Location', models.CharField(default=None, max_length=100)),
                ('PMV', models.BigIntegerField(default=None)),
                ('Raising', models.BigIntegerField(default=None)),
                ('Email', models.EmailField(default=None, max_length=254)),
                ('Assurance', models.CharField(choices=[('SEIS', 'SEIS'), ('EIS', 'EIS'), ('NONE', 'NONE')], default=None, max_length=6)),
                ('Stage', models.CharField(choices=[('Ideation/Angel', 'Ideation/Angel'), ('Pre-Seed', 'Pre-Seed'), ('Seed', 'Seed'), ('Series-A', 'Series-A'), ('Series-B', 'Series-B'), ('Series-C', 'Series-C'), ('Series-D', 'Series-D'), ('Mezzanine Round', 'Mezzanine Round'), ('IPO', 'IPO')], default=None, max_length=20)),
                ('upload', models.FileField(upload_to='uploads/')),
            ],
        ),
    ]