# Generated by Django 5.0.4 on 2024-05-13 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='text_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]
