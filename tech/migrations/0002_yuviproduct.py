# Generated by Django 3.0.5 on 2021-02-02 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yuviproduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=120)),
                ('oldcost', models.CharField(max_length=120)),
                ('newcost', models.CharField(max_length=120)),
                ('like', models.CharField(max_length=120)),
            ],
        ),
    ]
