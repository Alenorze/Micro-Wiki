# Generated by Django 2.0.2 on 2018-02-13 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20180213_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='version',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='pages.Version'),
        ),
    ]
