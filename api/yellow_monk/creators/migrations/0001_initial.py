# Generated by Django 4.0.3 on 2022-07-16 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('creator_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('contact_number', models.CharField(max_length=12)),
                ('link_tree', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ItemTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('piece_id', models.IntegerField()),
                ('tag_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('piece_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
            ],
        ),
    ]