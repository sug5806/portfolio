# Generated by Django 2.2.2 on 2019-06-10 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20190608_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
