# Generated by Django 2.2.2 on 2019-06-29 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=60)),
                ('esal', models.FloatField()),
                ('eaddr', models.CharField(max_length=200)),
            ],
        ),
    ]
