# Generated by Django 2.1.1 on 2018-09-03 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='announced_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
