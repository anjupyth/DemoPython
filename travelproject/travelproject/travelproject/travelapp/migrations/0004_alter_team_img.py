# Generated by Django 4.1.7 on 2023-03-08 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0003_alter_team_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='img',
            field=models.ImageField(height_field='height', upload_to='pics', width_field='width'),
        ),
    ]
