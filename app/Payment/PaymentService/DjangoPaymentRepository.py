from functools import reduce
from operator import and_, or_
from typing import List

from .AbstractFilter import AbstractFilter
from app.Mappers.DjangoPaymentMapper import DjangoPaymentMapper
from .Schemas import PaymentFilter, PaymentSchema
from .PaymentRepository import PaymentRepository
from Payment.models import Payment


class DjangoPaymentRepository(PaymentRepository):
    """Класс предоставляющий доступ к данным платежа с помощью Django ORM"""
    model = Payment

    def create_payment(self, payment: PaymentSchema):
        payment = self.validate(payment)
        payment_model = self.model(create_date=payment.create_date,
                                   status_id=payment.status.id,
                                   payment_type_id=payment.payment_type.id,
                                   category_id=payment.category.id,
                                   subcategory_id=payment.subcategory.id,
                                   amount=payment.amount,
                                   comment=payment.comment)
        payment_model.save()
        payment.id = payment_model.id
        return payment

    def get_payments(
            self,
            payment_filter: AbstractFilter = None) -> List[PaymentSchema]:

        if payment_filter:
            payments = self.model.objects.filter(payment_filter.build())
        else:
            payments = self.model.objects.select_related(
                'subcategory', 'category').all()
        payments_dto = []
        for payment in payments:
            payments_dto.append(DjangoPaymentMapper.to_dto(payment))

        return payments_dto

    def get_payment(self, id):
        payment = self.model.objects.get(id=id)
        return DjangoPaymentMapper.to_dto(payment)

    def delete_payment(self, id) -> bool:
        payment = self.model.objects.get(id=id)
        if payment:
            try:
                payment.delete()
            except Exception:
                return False
            return True
        return False

    def update_payment(self, id, payment):
        payment = self.validate(payment)
        payment_model = self.model.objects.get(id=id)
        payment_model.create_date = payment.create_date
        payment_model.status_id = payment.status.id
        payment_model.payment_type_id = payment.payment_type.id
        payment_model.category_id = payment.category.id
        payment_model.subcategory_id = payment.subcategory.id
        payment_model.amount = payment.amount
        payment_model.comment = payment.comment
        payment_model.save()
        return payment
