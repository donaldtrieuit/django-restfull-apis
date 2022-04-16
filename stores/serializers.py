from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from stores.models import Store


class StoreSerializer(serializers.ModelSerializer):
    store_name = serializers.CharField(max_length=512, required=True,
                                       validators=[UniqueValidator(queryset=Store.objects.all())])
    share_secret_key = serializers.CharField(max_length=256, required=True)

    class Meta:
        model = Store
        fields = ['id', 'store_id', 'store_name', 'share_secret_key', 'create_date', 'title', 'url',
                  'icon_url', 'listing_active_count', 'num_favorers', 'transaction_sold_count',
                  'review_average', 'review_count', 'activate', 'user']
        read_only_fields = ['store_id', 'create_date', 'title', 'url',
                            'icon_url', 'listing_active_count', 'num_favorers', 'transaction_sold_count',
                            'review_average', 'review_count', 'activate', 'user']
        extra_kwargs = {'store_api_key': {'write_only': True},
                        'share_secret_key': {'write_only': True}}
