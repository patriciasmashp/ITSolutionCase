from abc import ABC, abstractmethod
from typing import List, Any

from .Schemas import PaymentSchema


class AbstractFilter(ABC):
    """Абстрактный класс для фильтрации платежей для защиты репозитория от изменений"""
    @abstractmethod
    def build(self, payments: List[PaymentSchema]) -> Any:
        pass
