# Generated by Django 3.0.3 on 2020-06-15 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200616_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(null=True, verbose_name='内容'),
        ),
    ]
