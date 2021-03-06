# Generated by Django 2.0.2 on 2018-02-13 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release', models.CharField(max_length=5)),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField(max_length=2048)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('current', models.BooleanField(default=False, verbose_name='Current')),
            ],
            options={
                'ordering': ['-current'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='version',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pages.Version'),
        ),
    ]
