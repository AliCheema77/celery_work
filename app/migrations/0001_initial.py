# Generated by Django 3.2.11 on 2022-01-11 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('schedule_time', models.DateTimeField()),
                ('thrashed', models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly')], max_length=10)),
            ],
        ),
    ]
