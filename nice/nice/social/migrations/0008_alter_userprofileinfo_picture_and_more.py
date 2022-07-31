# Generated by Django 4.0 on 2022-01-18 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0007_alter_userprofileinfo_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='picture',
            field=models.ImageField(upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='portfolio',
            field=models.URLField(),
        ),
    ]
