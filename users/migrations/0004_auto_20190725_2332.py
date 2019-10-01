# Generated by Django 2.1.5 on 2019-07-26 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190725_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='teamname',
            field=models.CharField(default='Sharks', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='roster92',
            field=models.ForeignKey(default='Yianni Diakomihalis', on_delete=django.db.models.deletion.CASCADE, to='vws_main.FS_Wrestler'),
        ),
    ]