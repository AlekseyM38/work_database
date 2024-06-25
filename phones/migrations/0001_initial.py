# Generated by Django 5.0.6 on 2024-06-10 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='phone_images/')),
                ('release_date', models.DateField()),
                ('lte_exists', models.BooleanField(default=False)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
