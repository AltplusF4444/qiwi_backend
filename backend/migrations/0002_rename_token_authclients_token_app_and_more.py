# Generated by Django 4.0.4 on 2022-11-12 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authclients',
            old_name='token',
            new_name='token_app',
        ),
        migrations.AddField(
            model_name='authclients',
            name='token_qiwi',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
