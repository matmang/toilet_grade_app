# Generated by Django 4.0.6 on 2022-08-02 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Toilet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=140)),
                ('address', models.CharField(max_length=140)),
                ('gender', models.CharField(choices=[('MAN', 'MAN'), ('WOMAN', 'WOMAN')], max_length=5)),
                ('isBisexual', models.BooleanField(default=False)),
                ('toiletNum', models.IntegerField(default=0, help_text='대변기의 숫자', null=True)),
                ('urinalNum', models.IntegerField(default=0, help_text='소변기의 숫자', null=True)),
                ('disabledToiletNum', models.IntegerField(default=0, help_text='장애인용 대변기 숫자', null=True)),
                ('disabledUrinalNum', models.IntegerField(default=0, help_text='장애인용 소변기 숫자', null=True)),
                ('childToiletNum', models.IntegerField(default=0, help_text='어린이용 대변기 숫자', null=True)),
                ('childUrinalNum', models.IntegerField(default=0, help_text='어린이용 소변기 숫자', null=True)),
                ('managementAgency', models.CharField(help_text='설치 기관명', max_length=140)),
                ('phoneNumber', models.CharField(max_length=11)),
                ('openTime', models.CharField(max_length=140)),
                ('installationDate', models.CharField(max_length=140)),
                ('latitude', models.DecimalField(decimal_places=2, help_text='위도', max_digits=500)),
                ('longitude', models.DecimalField(decimal_places=2, help_text='경도', max_digits=500)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
