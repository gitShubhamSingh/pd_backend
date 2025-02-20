from rest_framework import serializers
from .models import AdminModel

class AdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = AdminModel
        fields = ['email','password']