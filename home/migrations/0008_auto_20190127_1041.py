# Generated by Django 2.1.4 on 2019-01-27 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20190125_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='describe',
            field=models.TextField(null=True),
        ),
    ]
