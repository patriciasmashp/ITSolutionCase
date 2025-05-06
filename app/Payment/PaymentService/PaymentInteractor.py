from datetime import datetime
from typing import List
from Directory.DirectoryService.Schemas import (CategorySchema, StatusSchema,
                                                SubcategorySchema, TypeSchema)
from .AbstractFilter import AbstractFilter
from .Schemas import PaymentSchema
from .DjangoPaymentRepository import PaymentRepository


class PaymentInteractor:
    """Класс инкапсулирует бизнес-логику работы с платежами"""

    def __init__(self, repository: PaymentRepository):
        self.repository: PaymentRepository = repository()

    def create_and_save_payment(self,
                                status: StatusSchema,
                                payment_type: TypeSchema,
                                category: CategorySchema,
                                subcategory: SubcategorySchema,
                                amount: float,
                                create_date: datetime = datetime.now(),
                                comment: str = ''):

        payment = PaymentSchema(payment_type=payment_type,
                                category=category,
                                amount=amount,
                                comment=comment,
                                subcategory=subcategory,
                                create_date=create_date,
                                status=status)
        payment = self.repository.create_payment(payment)

        return payment

    def get_payments(self):

        return self.repository.get_payments()

    def delete_payment(self, id: int):

        return self.repository.delete_payment(id)

    def get_payment(self, id: int):

        return self.repository.get_payment(id)

    def update_payment(self,
                       id: int,
                       status: StatusSchema,
                       payment_type: TypeSchema,
                       category: CategorySchema,
                       subcategory: SubcategorySchema,
                       amount: float,
                       create_date: datetime = datetime.now(),
                       comment: str = ''):
        payment = PaymentSchema(id=id,
                                payment_type=payment_type,
                                category=category,
                                amount=amount,
                                comment=comment,
                                subcategory=subcategory,
                                create_date=create_date,
                                status=status)
        return self.repository.update_payment(id, payment)

    def filter_payments(self,
                        filter_data: AbstractFilter) -> List[PaymentSchema]:
        return self.repository.get_payments(filter_data)
