# Generated by Django 4.2.6 on 2023-10-10 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_alter_region_parent_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='parent_region',
            field=models.ManyToManyField(blank=True, related_name='region_parent', to='user_profile.region', verbose_name='Parent region'),
        ),
    ]