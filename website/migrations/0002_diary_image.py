# Generated by Django 3.2 on 2021-06-15 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='image',
            field=models.ImageField(default='diary_thumbnail.jpg', upload_to='diary_thumbnail'),
        ),
    ]
