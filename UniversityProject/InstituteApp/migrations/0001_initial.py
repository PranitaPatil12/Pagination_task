# Generated by Django 4.0 on 2022-01-02 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Institute_ID', models.IntegerField()),
                ('Institute_Name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=40)),
            ],
        ),
    ]
