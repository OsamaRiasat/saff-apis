# Generated by Django 3.2.5 on 2022-09-14 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QualityControl', '0039_alter_rmparameters_parameter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pmparameters',
            name='parameter',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productparameters',
            name='parameter',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]