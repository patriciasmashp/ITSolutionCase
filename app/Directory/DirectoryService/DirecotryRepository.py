from abc import ABC, abstractmethod
from typing import List

from .Schemas import (CategorySchema, TypeSchema, SubcategorySchema,
                      StatusSchema)


class DirecotryRepository(ABC):
    """Абстрактный класс репозитория для работы с типами,
    статусами и категориями"""

    @abstractmethod
    def create_type(name: str, categories: List[CategorySchema]):
        """Создание типа из DTO

        Args:
            name (str): имя типа
            categories (List[CategorySchema]): Список возможных категорий
        """
        pass

    @abstractmethod
    def get_types() -> List[TypeSchema]:
        """метод получает список всех Типов
        """
        pass

    @abstractmethod
    def get_categories_by_type(self, type_id: int) -> List[CategorySchema]:
        """Метод получает категории по id типа

        Args:
            type_id (int)
        """
        pass

    @abstractmethod
    def get_type_by_id(self, type_id: int) -> TypeSchema:
        """Метод получает тип по id

        Args:
            type_id (int)
        """
        pass

    @abstractmethod
    def get_category_by_id(self, category_id: int) -> CategorySchema:
        """Метод получает категорию по id

        Args:
            category_id (int)
        """
        pass

    @abstractmethod
    def get_subcategory_by_id(self, subcategory_id: int) -> SubcategorySchema:
        """Метод получает подкатегорию по id

        Args:
            subcategory_id (int)
        """
        pass

    @abstractmethod
    def get_status_by_id(self, status_id: int) -> StatusSchema:
        """Метод получает статус по id

        Args:
            status_id (int)
        """
        pass

    @abstractmethod
    def get_categories(self) -> List[CategorySchema]:
        """Метод получает список категорий
        """
        pass

    @abstractmethod
    def get_subcategories(self) -> List[SubcategorySchema]:
        """Метод получает список подкатегорий
        """
        pass

    @abstractmethod
    def get_statuses(self) -> List[StatusSchema]:
        """Метод получает список статусов
        """
        pass
