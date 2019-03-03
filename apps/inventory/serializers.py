from rest_framework_mongoengine import serializers
from .models import Setting

class SettingSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Setting
        fields = '__all__'