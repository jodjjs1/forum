# Generated by Django 3.1.7 on 2021-04-05 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userforum', '0002_articles_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='publish_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
