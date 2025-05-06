from .Schemas import PaymentSchema


class PaymentValidator():
    """Класс отвечающий за валидацию данных платежа"""
    def __init__(self, payment: PaymentSchema):
        self.payment = payment

    def validate(self) -> PaymentSchema:
        """Метод проверяет выполнение бизне-логики в объекте PaymentSchema

        Raises:
            ValueError: Ошбики валидации


        Returns:
            PaymentSchema
        """
        self.payment = self.normalize()
        if self.payment.amount < 0:
            raise ValueError("Amount must be greater than 0")
        if self.payment.category not in self.payment.payment_type.categories:
            raise ValueError("Category must be in payment type categories")
        if self.payment.subcategory not in self.payment.category.subcategories:
            raise ValueError("Subcategory must be in category subcategories")
        
        return self.payment

    def normalize(self) -> PaymentSchema:
        """Метод приводит к машиночитаемому виду данные из PaymentSchema

        Returns:
            PaymentSchema: _description_
        """
        if isinstance(self.payment.amount, str):
            self.payment.amount = self.payment.amount.replace('руб', '')
            self.payment.amount = self.payment.amount.replace('рублей', '')
            self.payment.amount = self.payment.amount.replace('р', '')
            self.payment.amount = self.payment.amount.replace('р.', '')
            self.payment.amount = self.payment.amount.strip()
        self.payment.amount = float(self.payment.amount)
        return self.payment