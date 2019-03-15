# Generated by Django 2.1.7 on 2019-03-08 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('confidence', models.PositiveSmallIntegerField()),
                ('version', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=100)),
                ('web_site', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='WebPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urls', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='applications',
            name='web_page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.WebPage'),
        ),
    ]
