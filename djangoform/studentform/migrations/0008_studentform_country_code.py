# Generated by Django 4.0.5 on 2022-06-28 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentform', '0007_remove_studentform_country_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentform',
            name='country_code',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
