# Generated by Django 4.1.1 on 2022-09-07 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mychatapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('LocalVideo', models.FileField(upload_to='video/%y')),
            ],
        ),
    ]