# Generated by Django 3.2.25 on 2024-06-30 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20240630_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
