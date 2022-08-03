# Generated by Django 4.0.6 on 2022-08-03 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toilet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toilet',
            name='childToiletNum',
        ),
        migrations.RemoveField(
            model_name='toilet',
            name='disabledToiletNum',
        ),
        migrations.RemoveField(
            model_name='toilet',
            name='toiletNum',
        ),
        migrations.AddField(
            model_name='toilet',
            name='manChildToiletNum',
            field=models.IntegerField(default=0, help_text='남자 어린이용 대변기 숫자', null=True),
        ),
        migrations.AddField(
            model_name='toilet',
            name='manDisabledToiletNum',
            field=models.IntegerField(default=0, help_text='남자 장애인용 대변기 숫자', null=True),
        ),
        migrations.AddField(
            model_name='toilet',
            name='manToiletNum',
            field=models.IntegerField(default=0, help_text='남성용 대변기의 숫자', null=True),
        ),
        migrations.AddField(
            model_name='toilet',
            name='womanChildToiletNum',
            field=models.IntegerField(default=0, help_text='여자 어린이용 대변기 숫자', null=True),
        ),
        migrations.AddField(
            model_name='toilet',
            name='womanDisabledToiletNum',
            field=models.IntegerField(default=0, help_text='여자 장애인용 대변기 숫자', null=True),
        ),
        migrations.AddField(
            model_name='toilet',
            name='womanToiletNum',
            field=models.IntegerField(default=0, help_text='여성용 대변기의 숫자', null=True),
        ),
    ]