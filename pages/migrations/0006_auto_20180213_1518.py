# Generated by Django 2.0.2 on 2018-02-13 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_article_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='version',
            old_name='version',
            new_name='article',
        ),
        migrations.RemoveField(
            model_name='version',
            name='object_id',
        ),
        migrations.AddField(
            model_name='article',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
