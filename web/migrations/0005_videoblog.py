# Generated by Django 3.2.9 on 2021-11-22 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_feature_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='videoBlog/')),
                ('title', models.CharField(max_length=255)),
                ('logo', models.FileField(upload_to='videoBlog/')),
            ],
        ),
    ]
