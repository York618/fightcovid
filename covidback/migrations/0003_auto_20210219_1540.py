# Generated by Django 3.1.6 on 2021-02-19 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidback', '0002_auto_20210219_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='DNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='DeadNumber',
        ),
    ]
