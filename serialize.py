from django.db.models import fields
from rest_framework import serializers
from delegates.models import Delegates

class DelegatesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Delegates
        fields="__all__"