# Generated by Django 3.2.8 on 2023-01-16 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0003_article_composition'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]