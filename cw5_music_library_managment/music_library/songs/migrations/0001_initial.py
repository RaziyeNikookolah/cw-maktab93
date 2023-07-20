# Generated by Django 4.2.2 on 2023-06-23 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('genre', models.CharField(max_length=50)),
                ('biography', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('release_date', models.DateField()),
                ('cover_image', models.ImageField(upload_to='images/')),
                ('discription', models.TextField()),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='albums', to='songs.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('duration', models.DurationField()),
                ('track_number', models.IntegerField()),
                ('lyrics', models.TextField(unique=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='songs.album')),
            ],
            options={
                'unique_together': {('album', 'title')},
            },
        ),
    ]
