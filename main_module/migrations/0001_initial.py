# Generated by Django 4.2 on 2023-05-23 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio', models.FileField(upload_to='audio')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
