from Directory.DirectoryService.Schemas import StatusSchema, SubcategorySchema, TypeSchema, CategorySchema
from Directory.models import Status, Subcategory, Type, Category


class DjangoDirectoryMapper:
    """Класс предоставляет статические методы для преобразования данных из модели в DTO и наоборот."""

    def typeToDTO(type_model: Type):
        categories = []
        for category in type_model.categories.all():
            categories.append(DjangoDirectoryMapper.categoryToDTO(category))
        return TypeSchema(id=type_model.id,
                          name=type_model.name,
                          categories=categories)

    def categoryToDTO(category_model: Category):
        subcategories = []
        for subcategory in category_model.subcategories.all():
            subcategories.append(
                DjangoDirectoryMapper.subcategoryToDTO(subcategory))
        return CategorySchema(id=category_model.id,
                              name=category_model.name,
                              subcategories=subcategories)

    def subcategoryToDTO(subcategory_model: Subcategory):
        return SubcategorySchema(id=subcategory_model.id,
                                 name=subcategory_model.name)

    def statusToDTO(status_model: Status):
        return StatusSchema(id=status_model.id, name=status_model.name)
