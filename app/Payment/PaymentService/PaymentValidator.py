from .Schemas import PaymentSchema


class PaymentValidator():
    """Класс отвечающий за валидацию данных платежа"""
    def __init__(self, payment: PaymentSchema):
        self.payment = payment

    def validate(self):
        self.payment = self.normalize()
        if self.payment.amount < 0:
            raise ValueError("Amount must be greater than 0")
        if self.payment.category not in self.payment.payment_type.categories:
            raise ValueError("Category must be in payment type categories")
        if self.payment.subcategory not in self.payment.category.subcategories:
            raise ValueError("Subcategory must be in category subcategories")
        
        return self.payment

    def normalize(self):
        self.payment.amount = float(self.payment.amount)
        return self.payment