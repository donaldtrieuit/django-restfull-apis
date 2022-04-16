# Generated by Django 4.0.4 on 2022-04-16 06:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('store_id', models.CharField(blank=True, max_length=64)),
                ('store_name', models.CharField(blank=True, max_length=512, unique=True)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(blank=True, default='', max_length=512, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('icon_url', models.URLField(blank=True, null=True)),
                ('listing_active_count', models.IntegerField(blank=True, default=0, null=True)),
                ('num_favorers', models.IntegerField(blank=True, default=0, null=True)),
                ('transaction_sold_count', models.IntegerField(default=0)),
                ('review_average', models.FloatField(blank=True, default=0.0, null=True)),
                ('review_count', models.IntegerField(blank=True, default=0, null=True)),
                ('api_key', models.CharField(default='', max_length=256)),
                ('share_secret_key', models.CharField(default='', max_length=256)),
                ('oauth_token', models.CharField(default='', max_length=256)),
                ('oauth_token_secret', models.CharField(default='', max_length=256)),
                ('temp_oauth_token_secret', models.CharField(blank=True, default='', max_length=256)),
                ('access_token', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('refresh_token', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('activate', models.BooleanField(default=False)),
                ('latest_updated', models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store', to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'verbose_name_plural': 'Store',
                'db_table': 'store',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='StoreUpdateTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_update_date', models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0))),
                ('order_update_date', models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0))),
                ('listing_update_date', models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0))),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.store')),
            ],
        ),
        migrations.AddIndex(
            model_name='store',
            index=models.Index(fields=['id'], name='store_id_59c602_idx'),
        ),
    ]
