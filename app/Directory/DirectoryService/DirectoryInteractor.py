from typing import List

from .DirecotryRepository import DirecotryRepository
from .Schemas import CategorySchema, StatusSchema, TypeSchema


class DirectoryInteractor:
    """Класс инкапсулирует бизнес-логику работы с типами,
    статусами и категориями"""

    def __init__(self, directory_repository: DirecotryRepository):
        self.directory_repository: DirecotryRepository = directory_repository()

    def create_type(self, name: str, categories: List[CategorySchema]):

        return self.directory_repository.create_type(name, categories)

    def get_type_by_id(self, type_id: int) -> TypeSchema:
        return self.directory_repository.get_type_by_id(type_id)

    def get_types(self) -> List[TypeSchema]:
        return self.directory_repository.get_types()

    def get_categories_by_type(self, type_id: int) -> List[CategorySchema]:
        return self.directory_repository.get_categories_by_type(
            type_id=type_id)

    def get_category_by_id(self, category_id: int) -> CategorySchema:
        return self.directory_repository.get_category_by_id(category_id)

    def get_subcategory_by_id(self, subcategory_id: int) -> CategorySchema:
        return self.directory_repository.get_subcategory_by_id(subcategory_id)

    def get_status_by_id(self, status_id: int) -> StatusSchema:
        return self.directory_repository.get_status_by_id(status_id)

    def get_statuses(self) -> List[StatusSchema]:
        return self.directory_repository.get_statuses()

    def get_categories(self) -> List[CategorySchema]:
        return self.directory_repository.get_categories()

    def get_subcategories(self) -> List[CategorySchema]:
        return self.directory_repository.get_subcategories()
