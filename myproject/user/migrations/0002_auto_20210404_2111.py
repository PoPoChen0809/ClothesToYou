# Generated by Django 3.1.7 on 2021-04-04 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes2you_user',
            name='Gender',
            field=models.CharField(choices=[('男', 'Male'), ('女', 'Female'), ('不願透漏', 'Null')], default='N', max_length=5),
        ),
    ]
