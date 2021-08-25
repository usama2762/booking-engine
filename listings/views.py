from datetime import datetime

from django.db.models import Q
from rest_framework import generics

from listings.models import BookingInfo, Reserved
from listings.serializers import BookingInfoSerializer, ReservedSerializer


class BookingInfoViewSet(generics.ListAPIView):
    """
    BookingInfoViewSet
    """
    serializer_class = BookingInfoSerializer

    def get_queryset(self):
        max_price = self.request.query_params.get('max_price')
        check_in = self.request.query_params.get('check_in')
        check_out = self.request.query_params.get('check_out')
        print(max_price, check_in, check_out)
        queryset = BookingInfo.objects.all()
        if max_price:
            queryset.filter(price__lte=max_price)
        if check_in and check_out:
            reserved_listing = Reserved.objects.filter(Q(check_in__lte=check_in, check_out__gte=check_in) | Q(check_in__lte=check_out, check_out__gte=check_out))
            print(len(reserved_listing))

            queryset = queryset.exclude(id__in=[item.booking_info.id for item in reserved_listing])
        return queryset.order_by('price')


class ReservedInfoViewSet(generics.ListCreateAPIView):
    """
    ReservedInfoViewSet
    """
    serializer_class = ReservedSerializer
    queryset = Reserved.objects.all()
