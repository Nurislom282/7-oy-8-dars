# Generated by Django 5.1.4 on 2025-01-15 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='ctegory',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='category/images/'),
        ),
    ]
