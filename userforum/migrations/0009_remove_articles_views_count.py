# Generated by Django 3.1.7 on 2021-05-01 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userforum', '0008_auto_20210501_2330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='views_count',
        ),
    ]
