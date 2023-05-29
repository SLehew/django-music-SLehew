# Generated by Django 4.2.1 on 2023-05-29 16:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0012_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='user_favorite',
            field=models.ManyToManyField(blank=True, default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]