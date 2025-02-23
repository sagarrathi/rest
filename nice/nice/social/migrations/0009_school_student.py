# Generated by Django 4.0 on 2022-01-20 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0008_alter_userprofileinfo_picture_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('principal', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='social.school')),
            ],
        ),
    ]
