# Generated by Django 3.1.2 on 2020-12-04 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keijiban',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/media'),
        ),
    ]