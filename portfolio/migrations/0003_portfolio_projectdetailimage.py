# Generated by Django 3.2 on 2023-08-24 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_portfolio_coverimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='projectdetailimage',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]