# Generated by Django 3.1.5 on 2021-09-11 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footprint', '0007_post_totalamount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='totalAmount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True),
        ),
    ]
