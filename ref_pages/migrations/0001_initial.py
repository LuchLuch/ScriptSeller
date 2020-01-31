# Generated by Django 2.2.7 on 2020-01-29 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Referer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_link', models.CharField(max_length=200)),
                ('describe_link', models.TextField()),
                ('free_test', models.BooleanField(default=True)),
                ('personal_proxy', models.BooleanField(default=True)),
                ('change_proxy', models.BooleanField(default=True)),
                ('public', models.BooleanField(default=True)),
                ('img', models.ImageField(default='img/q12.jpg', upload_to='ref_img/')),
            ],
            options={
                'db_table': 'ref_pages_referer',
            },
        ),
    ]
