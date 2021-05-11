import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class StockFilter(django_filters.FilterSet):

    start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    end_date = DateFilter(field_name="date_created", lookup_expr='1te')
    class Meta:
        model = Stock
        fields = '__all__'
        # exclude = ['']



