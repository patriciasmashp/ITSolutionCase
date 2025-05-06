from abc import ABC, abstractmethod

from .PaymentValidator import PaymentValidator

from .Schemas import PaymentFilter, PaymentSchema


class PaymentRepository(ABC):
    """Абстрактный класс для доступа к данным платежей"""
    schema = PaymentSchema
    validator = PaymentValidator

    @abstractmethod
    def create_payment():
        pass

    @abstractmethod
    def get_payments(payment_filter: PaymentFilter = None):
        pass

    @abstractmethod
    def delete_payment():
        pass

    @abstractmethod
    def get_payment(id: int):
        pass

    @abstractmethod
    def update_payment(id: int, payment: PaymentSchema):
        pass

    def validate(self, payment: PaymentSchema):
        return self.validator(payment).validate()
