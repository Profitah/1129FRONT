# Generated by Django 4.1.2 on 2022-10-29 00:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cashbookapp', '0036_remove_cashbook_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashbook',
            name='writer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
