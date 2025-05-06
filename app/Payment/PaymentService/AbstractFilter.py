from abc import ABC, abstractmethod
from typing import Any


class AbstractFilter(ABC):
    """Абстрактный класс для фильтрации платежей
    для защиты репозитория от изменений"""

    @abstractmethod
    def build(self) -> Any:
        """Метод собирает фильтр в удобочитаемый вид для репозитория

        Returns:
            Any: Объект воспринимаемый репозиторием
            (в случае django это фильтры Q)
        """
        pass
