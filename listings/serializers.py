from rest_framework import serializers

from listings.models import BookingInfo, Reserved


class BookingInfoSerializer(serializers.ModelSerializer):
    """
    BookingInfoSerializer
    """
    class Meta:

        model = BookingInfo
        fields = '__all__'


class ReservedSerializer(serializers.ModelSerializer):
    """
    ReservedSerializer
    """
    class Meta:

        model = Reserved
        fields = '__all__'
