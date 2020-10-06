# Generated by Django 3.1.1 on 2020-09-11 06:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200911_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 11, 12, 23, 3, 937103), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_series',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='main.tutorialseries', verbose_name='Series'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_slug',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='tutorialcategory',
            name='category_slug',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='tutorialseries',
            name='tutorial_category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='main.tutorialcategory', verbose_name='Category'),
        ),
    ]