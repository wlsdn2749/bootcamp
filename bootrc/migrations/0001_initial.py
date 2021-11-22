# Generated by Django 3.2.8 on 2021-11-22 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_num', models.AutoField(primary_key=True, serialize=False)),
                ('menu_catenum', models.IntegerField()),
                ('menu_name2', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Rest',
            fields=[
                ('rest_num', models.AutoField(primary_key=True, serialize=False)),
                ('rest_name', models.CharField(max_length=30)),
                ('rest_star', models.FloatField(default=5)),
                ('rest_location_lat', models.FloatField(default=0)),
                ('rest_location_lon', models.FloatField(default=0)),
                ('rest_recent_user', models.IntegerField(default=0)),
                ('rest_number_reviews', models.IntegerField(default=0)),
                ('rest_distance_fromBD', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='restaurant_image')),
                ('back_image', models.ImageField(blank=True, null=True, upload_to='restaurant_back_image')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=300)),
                ('rating', models.PositiveIntegerField(default=0)),
                ('menu_name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('like_count', models.PositiveIntegerField(default=0)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='bootrc.rest')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='RestMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rest_menu', models.CharField(max_length=30)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, max_length=400, null=True, upload_to='menu_image')),
                ('recommendmenu', models.FloatField(default=0)),
                ('rest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bootrc.rest')),
            ],
        ),
        migrations.CreateModel(
            name='Prefer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pref_like', models.IntegerField()),
                ('pref_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bootrc.restmenu')),
                ('user_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('rest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='bootrc.rest')),
            ],
        ),
    ]
