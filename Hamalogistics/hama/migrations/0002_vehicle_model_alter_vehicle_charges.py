# Generated by Django 4.1 on 2022-10-06 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hama', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='model',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='charges',
            field=models.IntegerField(max_length=255, null=True),
        ),
    ]
