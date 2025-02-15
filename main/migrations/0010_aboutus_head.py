# Generated by Django 5.0.6 on 2024-10-26 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_projecttype_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('marketing_percentage', models.DecimalField(decimal_places=0, max_digits=2)),
                ('digital_media', models.DecimalField(decimal_places=0, max_digits=2, null=True)),
                ('social_media_maneging', models.DecimalField(decimal_places=0, max_digits=2, null=True)),
                ('text2', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'AboutUs',
                'verbose_name_plural': 'AboutUs',
            },
        ),
        migrations.CreateModel(
            name='Head',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Head',
                'verbose_name_plural': 'Head',
            },
        ),
    ]
