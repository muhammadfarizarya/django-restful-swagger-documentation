from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework_mongoengine import viewsets
from .serializers import SettingSerializer
from .models import Setting


class SettingViewSet(viewsets.ModelViewSet):
    '''
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    '''
    lookup_field = 'id'
    serializer_class = SettingSerializer

    def get_queryset(self):
        return Setting.objects.all()

    def list(self, request, *args, **kwargs):
        """
        API for return List of Settings
        """
        return super(SettingViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        API for creating new setting
        """
        return super(SettingViewSet, self).create(request, *args, **kwargs)

    # @action(detail=False, methods=['patch'], name="Partial Create", url_path="create")
    # def partial_create(self, request, *args, **kwargs):
    #     """
    #     API for creating partial setting
    #     """
    #     return True

    def retrieve(self, request, *args, **kwargs):
        """
        API for get one setting
        """
        return super(SettingViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        API for update one setting
        """
        return super(SettingViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        API for partial update setting
        """
        return super(SettingViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        API for delete one setting
        """
        return super(SettingViewSet, self).destroy(request, *args, **kwargs)