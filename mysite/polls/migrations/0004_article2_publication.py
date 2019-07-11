# Generated by Django 2.2.2 on 2019-07-06 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_article_reporter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Article2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('publications', models.ManyToManyField(to='polls.Publication')),
            ],
            options={
                'ordering': ('headline',),
            },
        ),
    ]
