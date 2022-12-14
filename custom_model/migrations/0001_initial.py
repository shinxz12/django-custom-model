# Generated by Django 4.1.3 on 2022-11-27 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('discount_value', models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True)),
                ('discount_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=8, max_digits=10)),
                ('category', models.ManyToManyField(blank=True, to='custom_model.category')),
            ],
        ),
    ]
