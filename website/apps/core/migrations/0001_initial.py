# Generated by Django 2.2.6 on 2019-10-09 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('nick', models.TextField(unique=True)),
                ('email', models.TextField(unique=True)),
                ('avatar', models.TextField(blank=True, null=True)),
                ('status', models.TextField(choices=[('Not Approved', 'not_approved'), ('Approved', 'approved'), ('Banned', 'banned'), ('Suspended', 'suspended'), ('On_Hollyday', 'on_hollyday')])),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('register_date', models.DateTimeField()),
                ('reputation', models.IntegerField(blank=True, null=True)),
                ('impact', models.IntegerField(blank=True, null=True)),
                ('badges', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]