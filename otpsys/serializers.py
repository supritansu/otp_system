from rest_framework import serializers
from . import models


class sendOtpserializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    mobile_number = serializers.CharField(required=True)

    class Meta:
        model = models.Customer
        fields = [
            "id",
            "mobile_number",
        ]
        read_only_fields = [
            "id",
        ]
