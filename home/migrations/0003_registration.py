# Generated by Django 5.1.4 on 2024-12-22 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_event_reg_details_alter_event_rulebook_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('college', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('area_of_intrest', models.CharField(max_length=50)),
            ],
        ),
    ]
