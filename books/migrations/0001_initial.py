# Generated by Django 4.1.1 on 2022-09-12 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('translator', models.CharField(blank=True, max_length=100, null=True)),
                ('publisher', models.CharField(max_length=100)),
                ('year_of_publication', models.IntegerField()),
                ('number_of_pages', models.IntegerField()),
                ('language', models.CharField(choices=[('lge', 'persian'), ('lge', 'english')], default='persian', max_length=50)),
            ],
        ),
    ]
