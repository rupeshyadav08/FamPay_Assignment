# Generated by Django 4.1.6 on 2023-02-05 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListOfVideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, max_length=500, null=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('VideoId', models.CharField(max_length=150)),
                ('ChannelId', models.CharField(max_length=150)),
                ('ChannelName', models.CharField(max_length=100)),
                ('Duration', models.FloatField()),
                ('UploadDateTime', models.DateTimeField()),
                ('ThumbnailUrl', models.URLField()),
                ('VideoUrl', models.URLField()),
            ],
        ),
    ]
