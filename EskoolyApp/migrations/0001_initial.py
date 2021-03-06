# Generated by Django 3.0.5 on 2020-06-18 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('monthly_fees', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='InstituteInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute_name', models.CharField(max_length=40)),
                ('target_line', models.CharField(max_length=100)),
                ('logo', models.FileField(upload_to='images/')),
                ('phone', models.IntegerField()),
                ('website', models.URLField()),
                ('address', models.CharField(max_length=80)),
                ('location', models.CharField(choices=[('IND', 'India'), ('PAK', 'Pakistan'), ('ENG', 'England'), ('AUS', 'Australia'), ('SA', 'South Africa')], max_length=3)),
                ('rules', models.CharField(default='aaabbbbsbsbsb', max_length=1000)),
                ('addfee', models.CharField(default=' ', max_length=40)),
                ('regfee', models.CharField(default=' ', max_length=40)),
                ('artfee', models.CharField(default=' ', max_length=40)),
                ('transportfee', models.CharField(default=' ', max_length=40)),
                ('booksfee', models.CharField(default=' ', max_length=40)),
                ('uniformfee', models.CharField(default=' ', max_length=40)),
                ('fine', models.CharField(default=' ', max_length=40)),
                ('others', models.CharField(default=' ', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=40)),
                ('weightage', models.IntegerField()),
                ('class_name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='EskoolyApp.Classes')),
            ],
        ),
    ]
