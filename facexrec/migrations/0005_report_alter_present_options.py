# Generated by Django 4.1.6 on 2023-03-27 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facexrec', '0004_present'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('discription', models.CharField(max_length=1000)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='present',
            options={'ordering': ['enroll']},
        ),
    ]
