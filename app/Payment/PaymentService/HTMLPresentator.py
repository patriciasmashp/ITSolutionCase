from typing import List
from Payment.PaymentService.Schemas import PaymentSchema


class HTMLPresentator:
    """Класс предоставляет статические методы для преобразования данных и отправки на фронт"""
    def payment_list(data: List[PaymentSchema]):
        res = []
        for payment in data:
            payment_ser = HTMLPresentator.payment(payment)
            res.append(payment_ser)
        return res

    def payment(payment: PaymentSchema):

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
        

