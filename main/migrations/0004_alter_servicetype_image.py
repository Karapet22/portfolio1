# Generated by Django 5.0.6 on 2024-10-21 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_servicetype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicetype',
            name='image',
            field=models.ImageField(upload_to='media/ServiceImages'),
        ),
    ]
