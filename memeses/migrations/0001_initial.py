# Generated by Django 2.2.9 on 2020-01-17 14:00

from django.db import migrations, models
import memeses.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Memes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('meme_image', models.ImageField(upload_to=memeses.models.memes_file_name)),
                ('tags', models.ManyToManyField(to='memeses.Tags')),
            ],
        ),
    ]
