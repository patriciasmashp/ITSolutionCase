from typing import List
from .Schemas import CategorySchema, StatusSchema, SubcategorySchema, TypeSchema


class HTMLPresentator:
    """Класс предоставляет статические методы для преобразования данных и отправки на фронт"""
    def category_list(data: List[CategorySchema]):
        res = []
        for category in data:
            category_ser = HTMLPresentator.category(category)
            res.append(category_ser)
        return res

    def subcategory_list(data: List[SubcategorySchema]):
        res = []
        for category in data:
            category_ser = HTMLPresentator.subcategory(category)
            res.append(category_ser)
        return res

    def status_list(data: List[StatusSchema]):
        res = []
        for status in data:
            status_ser = HTMLPresentator.status(status)
            res.append(status_ser)
        return res

    def type_list(data: List[TypeSchema]):
        res = []
        for type in data:
            type_ser = HTMLPresentator.payment_type(type)
            res.append(type_ser)
        return res
    
    def payment_type(data: TypeSchema):
        return {'id': data.id, 'name': data.name}


    def status(data: StatusSchema):
        return {'id': data.id, 'name': data.name}

    def subcategory(data: SubcategorySchema):
        return {'id': data.id, 'name': data.name}

    def category(data: CategorySchema):
        return {'id': data.id, 'name': data.name}
