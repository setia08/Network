# Generated by Django 3.2.15 on 2023-01-07 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_post_content',
            name='author',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
