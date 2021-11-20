# Generated by Django 3.2.8 on 2021-11-18 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_recommend',
            name='amazon_link',
            field=models.CharField(default='https://www.amazon.com/', max_length=65535),
        ),
        migrations.AddField(
            model_name='product_recommend',
            name='product_name',
            field=models.CharField(default='Product Placeholder', max_length=200),
        ),
    ]
