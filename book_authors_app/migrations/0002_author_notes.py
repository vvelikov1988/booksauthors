# Generated by Django 3.0.7 on 2020-07-14 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='Old Values'),
            preserve_default=False,
        ),
    ]