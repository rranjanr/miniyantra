# Generated by Django 4.1.2 on 2024-12-19 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='reg_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='rulebook',
            field=models.FileField(upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='thumbnail',
            field=models.ImageField(upload_to='img/'),
        ),
    ]