# Generated by Django 4.1.6 on 2023-06-07 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.PositiveIntegerField()),
                ('pen_name', models.CharField(max_length=200)),
                ('journal', models.CharField(max_length=200)),
                ('active_date', models.DateField()),
            ],
        ),
    ]
