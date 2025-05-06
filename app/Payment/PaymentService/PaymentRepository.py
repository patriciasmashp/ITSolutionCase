from abc import ABC, abstractmethod
from typing import List

from .PaymentValidator import PaymentValidator

from .Schemas import PaymentFilter, PaymentSchema


class PaymentRepository(ABC):
    """Абстрактный класс для доступа к данным платежей"""
    schema = PaymentSchema
    validator = PaymentValidator

    @abstractmethod
    def create_payment(payment: PaymentSchema) -> PaymentSchema:
        """Метод создает платеж из DTO PaymentSchema и сохраняет его в БД
        """
        pass

    @abstractmethod
    def get_payments(
            payment_filter: PaymentFilter = None) -> List[PaymentSchema]:
        """Метод получает список ДДС используя фильтр

        Args:
            payment_filter (PaymentFilter, optional): DTO фильтра.
            По умолчанию None.

        Returns:
            List[PaymentSchema]: Список DTO ДДС
        """
        pass

    @abstractmethod
    def delete_payment(id: int) -> bool:
        """Метод удаляет ДДС по его Id
        В случае успешного удаления возвращает True,
        иначе False
        Args:
            id (int): id ДДС

        Returns:
            bool: В случае успешного удаления возвращает True,
        иначе False
        """
        pass

    @abstractmethod
    def get_payment(id: int) -> PaymentSchema:
        """Метод получает объект ДДС по его Id

        Args:
            id (int): Id записи в бд

        Returns:
            PaymentSchema: DTO ДДС
        """
        pass

    @abstractmethod
    def update_payment(id: int, payment: PaymentSchema) -> PaymentSchema:
        """Метод обновляет запись ДДС по ее Id

        Args:
            id (int): id записи в бд
            payment (PaymentSchema): DTO с новыми данными ДДС

        Returns:
            PaymentSchema: DTO ДДС
        """
        pass

    def validate(self, payment: PaymentSchema) -> PaymentSchema:
        """Метод запускает валидацию объекта ДДС

        Args:
            payment (PaymentSchema): DTO с данными ДДС

        Returns:
            PaymentSchema: В случае успешной проверки возвращает объект
        
        Raises:
            ValueError: В случае ошибок валидации
        """
        return self.validator(payment).validate()
