# Generated by Django 2.2.2 on 2019-06-20 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20190620_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notasactividad',
            name='valor',
            field=models.FloatField(),
        ),
    ]
