# Generated by Django 2.0.2 on 2018-02-13 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20180213_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='version',
        ),
        migrations.AddField(
            model_name='version',
            name='object_id',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='version',
            name='version',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='pages.Article'),
        ),
    ]
