import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from django_extensions.db.models import TimeStampedModel


class Store(TimeStampedModel, models.Model):
    store_id = models.CharField(max_length=64, blank=True)
    store_name = models.CharField(max_length=512, blank=True, unique=True)
    create_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=512, blank=True, null=True, default="")
    url = models.URLField(max_length=200, blank=True, null=True)
    icon_url = models.URLField(max_length=200, blank=True, null=True)
    listing_active_count = models.IntegerField(default=0, null=True, blank=True)
    num_favorers = models.IntegerField(default=0, null=True, blank=True)
    transaction_sold_count = models.IntegerField(default=0)
    review_average = models.FloatField(default=0.0, null=True, blank=True)
    review_count = models.IntegerField(default=0, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             to_field='username', related_name='store')
    api_key = models.CharField(max_length=256, blank=False, default="")
    share_secret_key = models.CharField(max_length=256, blank=False, default="")
    oauth_token = models.CharField(max_length=256, blank=False, default="")
    oauth_token_secret = models.CharField(max_length=256, blank=False, default="")
    temp_oauth_token_secret = models.CharField(max_length=256, blank=True, default="")
    access_token = models.CharField(max_length=256, blank=True, null=True, default="")
    refresh_token = models.CharField(max_length=256, blank=True, null=True, default="")
    activate = models.BooleanField(default=False)
    latest_updated = models.DateTimeField(auto_now=False, auto_now_add=False,
                                          default=datetime.datetime.utcfromtimestamp(0))

    class Meta:
        verbose_name_plural = 'Store'
        db_table = 'store'
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id']),
        ]

    def __str__(self):
        return self.store_name


class StoreUpdateTime(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    shop_update_date = models.DateTimeField(auto_now=False, auto_now_add=False,
                                            default=datetime.datetime.utcfromtimestamp(0))
    order_update_date = models.DateTimeField(auto_now=False, auto_now_add=False,
                                             default=datetime.datetime.utcfromtimestamp(0))
    listing_update_date = models.DateTimeField(auto_now=False, auto_now_add=False,
                                               default=datetime.datetime.utcfromtimestamp(0))
