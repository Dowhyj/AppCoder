# Generated by Django 4.0.5 on 2022-07-21 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0005_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='curso',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
