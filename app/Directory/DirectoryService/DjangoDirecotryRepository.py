from typing import List

from Directory.models import Type, Category, Subcategory, Status
from app.Mappers.DjangoDirectoryMapper import DjangoDirectoryMapper
from .DirecotryRepository import DirecotryRepository
from .Schemas import CategorySchema, TypeSchema


class DjangoDirecotryRepository(DirecotryRepository):
    """Класс репозитория для работы с моделями Django"""
    def create_type(self, name: str, categories: List[CategorySchema]):
        type_dto = TypeSchema(name=name, categories=categories)
        return type_dto

    def get_type_by_id(self, type_id: int):
        payment_type = Type.objects.get(id=type_id)
        return DjangoDirectoryMapper.typeToDTO(payment_type)

    def get_types(self):
        types = Type.objects.all()
        types_dto = []
        for payment_type in types:
            types_dto.append(DjangoDirectoryMapper.typeToDTO(payment_type))
        return types_dto

    def get_categories_by_type(self, type_id: int):
        categories = Type.objects.get(id=type_id).categories.all()
        categories_dto = []
        for category in categories:
            categories_dto.append(
                DjangoDirectoryMapper.categoryToDTO(category))
        return categories_dto

    def get_category_by_id(self, category_id: int):
        category = Category.objects.get(id=category_id)
        return DjangoDirectoryMapper.categoryToDTO(category)

    def get_subcategory_by_id(self, subcategory_id: int):
        subcategory = Subcategory.objects.get(id=subcategory_id)
        return DjangoDirectoryMapper.subcategoryToDTO(subcategory)

    def get_status_by_id(self, status_id: int):
        status = Status.objects.get(id=status_id)
        return DjangoDirectoryMapper.statusToDTO(status)

    def get_categories(self):
        categories = Category.objects.all()
        categories_dto = []
        for category in categories:
            categories_dto.append(
                DjangoDirectoryMapper.categoryToDTO(category))
        return categories_dto

    def get_subcategories(self):
        subcategories = Subcategory.objects.all()
        subcategories_dto = []
        for subcategory in subcategories:
            subcategories_dto.append(
                DjangoDirectoryMapper.subcategoryToDTO(subcategory))
        return subcategories_dto

    def get_statuses(self):
        statuses = Status.objects.all()
        statuses_dto = []
        for status in statuses:
            statuses_dto.append(DjangoDirectoryMapper.statusToDTO(status))
        return statuses_dto