from typing import List
from Payment.PaymentService.Schemas import PaymentSchema


class HTMLPresentator:
    """Класс предоставляет статические методы для преобразования данных
    и отправки в html"""

    def payment_list(data: List[PaymentSchema]) -> List[dict]:
        """Статический метод. Является оберткой payment для обработки списков

        Args:
            data (List[PaymentSchema]): Список DTO с данными ДДС

        Returns:
            List[dict]: Список словарей готовых для отправки в html
        """
        res = []
        for payment in data:
            payment_ser = HTMLPresentator.payment(payment)
            res.append(payment_ser)
        return res

    def payment(payment: PaymentSchema) -> dict:
        """Статический метод.
        Подготавливает данные из DTO в простой словарь для обработки в html

        Args:
            payment (PaymentSchema): DTO с данными ДДС

        Returns:
            dict: Словарь с данными ДДС
        """
        return {
            "id": payment.id,
            "create_date": payment.hr_create_date,
            "status": payment.status.name,
            "payment_type": payment.payment_type.name,
            "category": payment.category.name,
            "subcategory": payment.subcategory.name,
            "amount": str(payment.amount) + " руб.",
            "comment": payment.comment
        }
