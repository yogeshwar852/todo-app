# Generated by Django 2.2.7 on 2020-05-01 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=500)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
