# Generated by Django 2.1.1 on 2018-09-03 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180903_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
