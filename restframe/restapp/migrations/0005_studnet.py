# Generated by Django 2.2.2 on 2019-07-01 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0004_update_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studnet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('S_Name', models.CharField(max_length=30)),
                ('S_Class', models.TextField(max_length=10)),
                ('s_Age', models.IntegerField(max_length=2)),
                ('s_mobile', models.IntegerField(max_length=10)),
            ],
        ),
    ]