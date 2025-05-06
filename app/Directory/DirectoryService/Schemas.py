from typing import List
from dataclasses import dataclass, field


@dataclass
class StatusSchema():
    """DTO статуса ДДС"""
    id: int | None
    name: str


@dataclass
class SubcategorySchema():
    """DTO подкатегории ДДС"""
    id: int | None
    name: str


@dataclass
class CategorySchema():
    """DTO категории ДДС"""
    id: int | None
    name: str
    subcategories: List[SubcategorySchema] = field(default_factory=[])


@dataclass
class TypeSchema():
    """DTO типа ДДС"""
    id: int | None
    name: str
    categories: List[CategorySchema] = field(default_factory=[])
