# Generated by Django 2.2.2 on 2019-06-23 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20190623_0158'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='matricula',
            options={'ordering': ['-alumno']},
        ),
    ]
