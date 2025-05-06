from typing import List
from Directory.DirectoryService.DirectoryInteractor import DirectoryInteractor
from Directory.DirectoryService.DjangoDirecotryRepository import DjangoDirecotryRepository
from Directory.DirectoryService.Schemas import TypeSchema, CategorySchema, StatusSchema, SubcategorySchema

from Payment.PaymentService.DjangoPaymentFilter import DjangoPaymentFilter
from Payment.PaymentService.DjangoPaymentRepository import DjangoPaymentRepository
from Payment.PaymentService.PaymentInteractor import PaymentInteractor
from Payment.PaymentService.Schemas import PaymentSchema
from app.Mappers.DjangoPaymentMapper import DjangoPaymentMapper


class Dispathcer:
    """Класс реализует паттерн Singleton
    и предоставляет единый интерфейс для работы с сервисами"""
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

    def __init__(self):
        self.directory_interactor = DirectoryInteractor(
            DjangoDirecotryRepository)
        self.payment_interactor = PaymentInteractor(DjangoPaymentRepository)

    def get_payments(self) -> List[PaymentSchema]:

        return self.payment_interactor.get_payments()

    def get_payment(self, id: int) -> PaymentSchema:
        return self.payment_interactor.get_payment(id)

    def delete_payment(self, id: int) -> List[PaymentSchema]:
        return self.payment_interactor.delete_payment(id)

    def get_types(self) -> List[TypeSchema]:
        return self.directory_interactor.get_types()

    def get_categories_by_type(self, type_id: int) -> List[CategorySchema]:
        return self.directory_interactor.get_categories_by_type(type_id)

    def fetch_directory_and_create_payment(self,
                                           payment: dict) -> PaymentSchema:
        payment_type = self.directory_interactor.get_type_by_id(
            payment['payment_type'])
        category = self.directory_interactor.get_category_by_id(
            payment['category'])
        subcategory = self.directory_interactor.get_subcategory_by_id(
            payment['subcategory'])
        status = self.directory_interactor.get_status_by_id(payment['status'])

        return self.payment_interactor.create_and_save_payment(
            status=status,
            payment_type=payment_type,
            category=category,
            subcategory=subcategory,
            amount=payment['amount'],
            comment=payment['comment'] if 'comment' in payment else '')

    def fetch_directory_and_update_payment(self,
                                           payment: dict) -> PaymentSchema:
        payment_type = self.directory_interactor.get_type_by_id(
            payment['payment_type'])
        category = self.directory_interactor.get_category_by_id(
            payment['category'])
        subcategory = self.directory_interactor.get_subcategory_by_id(
            payment['subcategory'])
        status = self.directory_interactor.get_status_by_id(payment['status'])

        return self.payment_interactor.update_payment(
            id=payment['id'],
            status=status,
            payment_type=payment_type,
            category=category,
            subcategory=subcategory,
            amount=payment['amount'],
            comment=payment['comment'])

    def get_categories(self) -> List[CategorySchema]:
        return self.directory_interactor.get_categories()

    def get_subcategories(self) -> List[SubcategorySchema]:
        return self.directory_interactor.get_subcategories()

    def get_statuses(self) -> List[StatusSchema]:
        return self.directory_interactor.get_statuses()

    def filter_payments(self, filter: dict) -> List[PaymentSchema]:
        filter = DjangoPaymentMapper.filter_to_dto(filter)
        django_filter = DjangoPaymentFilter(filter)
        return self.payment_interactor.filter_payments(django_filter)
