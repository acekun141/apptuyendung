# Generated by Django 2.1.4 on 2019-01-24 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0003_auto_20190124_1111'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfomationEnterprise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=200)),
                ('local', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=500)),
                ('select', models.CharField(choices=[('1', 'Dưới 10 nhân viên'), ('2', 'Từ 10-49 nhân viên'), ('3', 'Từ 50-99 nhân viên'), ('4', 'Từ 100-499 nhân viên'), ('5', 'Từ 500-1000 nhân viên'), ('6', 'Trên 1000 nhân viên')], max_length=1)),
                ('describe', models.TextField()),
            ],
        ),
    ]