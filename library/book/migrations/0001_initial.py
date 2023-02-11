# Generated by Django 4.1 on 2023-02-11 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('name', models.CharField(blank=True, max_length=128)),
                ('description', models.CharField(blank=True, max_length=256)),
                ('count', models.IntegerField(default=10)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('authors', models.ManyToManyField(related_name='books', to='author.author')),
            ],
        ),
    ]
