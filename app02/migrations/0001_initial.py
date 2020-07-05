# Generated by Django 2.0.3 on 2020-07-03 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=32, verbose_name='主机表')),
                ('ip', models.GenericIPAddressField(verbose_name='IP')),
            ],
        ),
    ]