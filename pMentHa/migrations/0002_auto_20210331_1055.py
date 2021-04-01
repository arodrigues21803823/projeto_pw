# Generated by Django 3.1.6 on 2021-03-31 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pMentHa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='report',
            name='test',
        ),
        migrations.AddField(
            model_name='report',
            name='resolution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pMentHa.resolution'),
        ),
    ]