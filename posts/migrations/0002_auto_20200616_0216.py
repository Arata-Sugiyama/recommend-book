# Generated by Django 3.0.3 on 2020-06-15 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='impression',
            field=models.TextField(blank=True, null=True, verbose_name='感想'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(null=True, verbose_name='あらすじ'),
        ),
    ]
