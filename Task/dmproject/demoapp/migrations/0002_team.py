# Generated by Django 5.0 on 2024-01-02 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=250)),
                ('img1', models.ImageField(upload_to='pics')),
                ('desc1', models.TextField()),
            ],
        ),
    ]
