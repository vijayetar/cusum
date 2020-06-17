# Generated by Django 3.0.7 on 2020-06-17 21:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.TextField(choices=[('oral_ETT', 'oral intubation'), ('nasal_ETT', 'nasal intubation'), ('PICC', 'PICC placement'), ('UAC', 'Umbilical artery line placement'), ('UVC', 'Umbilical vein line placement')], max_length=10, verbose_name='Select name of event')),
                ('event_date', models.DateField(default=django.utils.timezone.now, verbose_name='Enter date of event')),
                ('event_outcome', models.IntegerField(choices=[(1, 'SUCCESS'), (0, 'FAILURE')], verbose_name='Select outcome')),
                ('event_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]