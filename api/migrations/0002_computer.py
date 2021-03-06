# Generated by Django 2.0.6 on 2020-07-07 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('brand', models.CharField(max_length=30, verbose_name='品牌')),
            ],
            options={
                'db_table': 'hdy_computer',
            },
        ),
    ]
