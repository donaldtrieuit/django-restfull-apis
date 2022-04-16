from rest_framework import viewsets

from stores.models import Store

from .serializers import StoreSerializer


class StoreApiView(viewsets.ModelViewSet):
    serializer_class = StoreSerializer

    def get_queryset(self):
        qs = Store.objects.all()
        if self.request.user.is_superuser is False:
            qs = qs.filter(user=self.request.user)
        return qs

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)