# Generated by Django 2.2.7 on 2020-02-03 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ref_pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referer',
            name='img',
            field=models.ImageField(default='img/q12.jpg', upload_to=''),
        ),
    ]
