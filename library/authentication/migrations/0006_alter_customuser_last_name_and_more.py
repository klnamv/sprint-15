# Generated by Django 4.1 on 2023-02-10 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_customuser_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='middle_name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]