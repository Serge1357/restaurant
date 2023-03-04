# Generated by Django 4.1.6 on 2023-02-11 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, unique=True)),
                ('position', models.SmallIntegerField(unique=True)),
                ('is_visible', models.BooleanField(unique=True)),
            ],
            options={
                'ordering': ('position',),
            },
        ),
    ]