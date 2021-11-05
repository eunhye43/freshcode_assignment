# Generated by Django 3.2.9 on 2021-11-05 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=256)),
                ('is_sold', models.BooleanField(default=True)),
                ('badge', models.CharField(default='NEW', max_length=16)),
            ],
            options={
                'db_table': 'menus',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=32)),
                ('menu_id', models.ForeignKey(db_column='menu_id', on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='menus.menu')),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('size', models.CharField(max_length=16)),
                ('price', models.IntegerField()),
                ('is_sold', models.BooleanField(default=True)),
                ('menu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='menus.menu')),
            ],
            options={
                'db_table': 'items',
            },
        ),
    ]
