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
                                comment: str = '') -> PaymentSchema:
        """Метод создает объект payment и сохраняет его

        Args:
            status (StatusSchema): DTO статуса
            payment_type (TypeSchema): DTO типа
            category (CategorySchema): DTO категории
            subcategory (SubcategorySchema): DTO подкатегории
            amount (float): Сумма
            create_date (datetime, optional): Дата создания. Defaults to datetime.now().
            comment (str, optional): Комментарий. Defaults to ''.

        Returns:
            PaymentSchema: DTO с данными ДДС
        """
        payment = PaymentSchema(payment_type=payment_type,
                                category=category,
                                amount=amount,
                                comment=comment,
                                subcategory=subcategory,
                                create_date=create_date,
                                status=status)
        payment = self.repository.create_payment(payment)

        return payment

    def get_payments(self) -> List[PaymentSchema]:
        """Метод возвращает список ДДС 

        Returns:
            List[PaymentSchema]: Список DTO c данными ДДС
        """

        return self.repository.get_payments()

    def delete_payment(self, id: int) -> bool:
        """Удаление ДДС по его id

        Args:
            id (int): id ДДС записи в бд

        Returns:
            bool: True в случае успешного удаления
            и False в ином случае
        """
        return self.repository.delete_payment(id)

    def get_payment(self, id: int) -> PaymentSchema:
        """Получить ДДС по его id

        Args:
            id (int): id ДДС записи в бд

        Returns:
            PaymentSchema: DTO с данными ДДС
        """
        return self.repository.get_payment(id)

    def update_payment(self,
                       id: int,
                       status: StatusSchema,
                       payment_type: TypeSchema,
                       category: CategorySchema,
                       subcategory: SubcategorySchema,
                       amount: float,
                       create_date: datetime = datetime.now(),
                       comment: str = '') -> PaymentSchema:
        """_summary_

        Args:
            id (int): id обновляемой записи
            status (StatusSchema): DTO статуса
            payment_type (TypeSchema): DTO типа
            category (CategorySchema): DTO категории
            subcategory (SubcategorySchema): DTO подкатегории
            amount (float): Сумма
            create_date (datetime, optional): Дата создания. Defaults to datetime.now().
            comment (str, optional): Комментарий. Defaults to ''.

        Returns:
            PaymentSchema: DTO с данными ДДС
        """
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
        """Фильтрация ДДС

        Args:
            filter_data (AbstractFilter): Объект-предок AbstractFilter реализующий метод build

        Returns:
            List[PaymentSchema]: Отфильтрованный список DTO c данными ДДС
        """
        return self.repository.get_payments(filter_data)
