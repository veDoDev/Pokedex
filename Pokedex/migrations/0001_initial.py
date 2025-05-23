# Generated by Django 5.1.5 on 2025-04-20 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('image_url', models.TextField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('hp', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('speed', models.IntegerField()),
            ],
            options={
                'db_table': 'pokemon',
                'ordering': ['id'],
                'managed': False,
            },
        ),
    ]
