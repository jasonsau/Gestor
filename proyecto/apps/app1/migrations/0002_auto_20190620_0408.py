# Generated by Django 2.2.2 on 2019-06-20 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notasactividad',
            name='valor',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
