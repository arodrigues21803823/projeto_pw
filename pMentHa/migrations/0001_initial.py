# Generated by Django 3.2.3 on 2021-06-24 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.CharField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=128)),
                ('contact', models.IntegerField()),
                ('birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=64)),
                ('gender', models.CharField(max_length=64)),
                ('nacionality', models.CharField(max_length=64)),
                ('date', models.DateField()),
                ('disease', models.CharField(max_length=64)),
                ('disease2', models.TextField(blank=True, max_length=258)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('multipla', models.BooleanField(default=False)),
                ('category', models.TextField(max_length=1000)),
                ('text', models.TextField(max_length=1000)),
                ('explain', models.TextField(blank=True, max_length=1000)),
                ('cover', models.TextField(blank=True, max_length=100)),
                ('stimulus', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('statement', models.TextField(max_length=1000)),
                ('advisor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='advisor', to='pMentHa.advisor')),
                ('questions', models.ManyToManyField(blank=True, related_name='questions', to='pMentHa.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Resolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patient', to='pMentHa.patient')),
                ('test', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='test', to='pMentHa.test')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000)),
                ('advisor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pMentHa.advisor')),
                ('resolution', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pMentHa.resolution')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pMentHa.question')),
                ('test', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pMentHa.test')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='resolutions',
            field=models.ManyToManyField(blank=True, related_name='resolutions', to='pMentHa.Resolution'),
        ),
        migrations.AddField(
            model_name='patient',
            name='tests',
            field=models.ManyToManyField(blank=True, related_name='tests', to='pMentHa.Test'),
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.TextField(max_length=1000)),
                ('order', models.IntegerField()),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pMentHa.question')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=258)),
                ('quotation', models.CharField(blank=True, max_length=64, null=True)),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='respostas', to='pMentHa.question')),
                ('resolution', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resolution', to='pMentHa.resolution')),
            ],
        ),
    ]
