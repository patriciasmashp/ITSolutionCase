from abc import ABC, abstractmethod
from typing import List

from .Schemas import CategorySchema, TypeSchema


class DirecotryRepository(ABC):
    """Абстрактный класс репозитория для работы с типами, статусами и категориями"""
    @abstractmethod
    def create_type(name: str, categories: List[CategorySchema]):
        pass

    @abstractmethod
    def get_types():
        pass

    @abstractmethod
    def get_categories_by_type(self, type_id: int):
        pass

    @abstractmethod
    def get_type_by_id(self, type_id: int):
        pass

    @abstractmethod
    def get_category_by_id(self, category_id: int):
        pass

    @abstractmethod
    def get_subcategory_by_id(self, subcategory_id: int):
        pass

    @abstractmethod
    def get_status_by_id(self, status_id: int):
        pass

    @abstractmethod
    def get_categories(self):
        pass

    @abstractmethod
    def get_subcategories(self):
        pass

    @abstractmethod
    def get_statuses(self):
        pass
