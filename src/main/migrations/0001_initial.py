# Generated by Django 4.2.3 on 2023-07-09 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence', models.CharField(max_length=200)),
                ('pronunciation_sound_url', models.CharField(max_length=1000)),
            ],
        ),
    ]
