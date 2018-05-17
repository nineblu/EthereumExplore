# Generated by Django 2.0.5 on 2018-05-16 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blocks',
            fields=[
                ('block_number', models.IntegerField(primary_key=True, serialize=False)),
                ('block_hash', models.CharField(max_length=100)),
                ('timestamp', models.CharField(max_length=100)),
                ('prev_block_hash', models.CharField(max_length=100)),
                ('nonce', models.CharField(max_length=100)),
                ('miner_addr', models.CharField(max_length=100)),
                ('difficulty', models.CharField(max_length=100)),
                ('size_bytes', models.IntegerField()),
                ('extra_data', models.CharField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='number_tx_in_block',
            fields=[
                ('block_number', models.IntegerField(primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('block_number', models.IntegerField()),
                ('block_hash', models.CharField(max_length=100)),
                ('tx_from', models.CharField(max_length=100)),
                ('tx_hash', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('tx_index', models.CharField(max_length=100)),
                ('tx_input', models.CharField(max_length=10000)),
                ('tx_value', models.CharField(max_length=100)),
                ('tx_type', models.IntegerField()),
                ('nonce', models.IntegerField()),
                ('tx_to', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tx_Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tx_hash', models.CharField(max_length=100)),
                ('block_number', models.IntegerField()),
                ('block_hash', models.CharField(max_length=100)),
            ],
        ),
    ]