from functools import reduce
from operator import and_
from .AbstractFilter import AbstractFilter
from .Schemas import PaymentFilter
from django.db.models import Q


class DjangoPaymentFilter(AbstractFilter):
    """Класс для фильтрации платежей c помощью django.db.models.Q"""
    def __init__(self, payment_filter: PaymentFilter):
        self.timeEnd = payment_filter.timeEnd
        self.timeStart = payment_filter.timeStart
        self.status_id = payment_filter.status_id
        self.category_id = payment_filter.category_id
        self.subcategory_id = payment_filter.subcategory_id
        self.payment_type_id = payment_filter.payment_type_id

    def build(self):
        filters_queries = []

        if self.payment_type_id:
            filters_queries.append(Q(payment_type_id=self.payment_type_id))
        if self.category_id:
            filters_queries.append(Q(category_id=self.category_id))
        if self.subcategory_id:
            filters_queries.append(Q(subcategory_id=self.subcategory_id))
        if self.status_id:
            filters_queries.append(Q(status_id=self.status_id))
        if self.timeEnd and self.timeStart:
            filters_queries.append(
                Q(create_date__range=(self.timeStart, self.timeEnd)))
        elif self.timeEnd:
            filters_queries.append(Q(create_date__lte=self.timeEnd))
        elif self.timeStart:
            filters_queries.append(Q(create_date__gte=self.timeStart))
        if len(filters_queries) == 0:
            return Q()
        return reduce(and_, filters_queries)
