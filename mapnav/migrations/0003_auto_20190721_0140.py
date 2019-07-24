# Generated by Django 2.2.2 on 2019-07-20 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapnav', '0002_auto_20190708_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('amount', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='user_info',
        ),
    ]
