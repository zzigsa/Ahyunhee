# Generated by Django 2.2.5 on 2019-11-28 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='zzigsa',
            field=models.CharField(choices=[('not yet', 'Not yet'), ('approved', 'Approved'), ('denied', 'Denied')], default='denied', max_length=10),
        ),
    ]
