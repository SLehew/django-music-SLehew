# Generated by Django 4.2.1 on 2023-05-25 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_remove_album_artist_remove_album_songs_album_track_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='track',
        ),
        migrations.RemoveField(
            model_name='song',
            name='record',
        ),
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='music.album'),
        ),
    ]