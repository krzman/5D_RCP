# Generated by Django 5.1.3 on 2024-11-20 11:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_rcp_5d', '0002_alter_users_rfid_number'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RCPList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('construcion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_rcp_5d.construcion')),
                ('rfid_device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_rcp_5d.rcpdevice')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
