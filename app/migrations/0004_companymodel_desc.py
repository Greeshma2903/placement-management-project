# Generated by Django 4.1.3 on 2022-12-19 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_jobapplication_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='companymodel',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]