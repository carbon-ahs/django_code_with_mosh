# Generated by Django 3.2 on 2021-10-27 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip_code',
            field=models.CharField(default='00', max_length=255),
            preserve_default=False,
        ),
    ]
