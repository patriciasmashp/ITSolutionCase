from Payment.models import Payment
from Payment.PaymentService.Schemas import PaymentFilter, PaymentSchema
from Directory.DirectoryService.Schemas import CategorySchema, StatusSchema, SubcategorySchema, TypeSchema


class DjangoPaymentMapper:
    """Класс предоставляет статические методы для преобразования данных из модели в DTO и наоборот."""

    def to_dto(payment_model: Payment) -> PaymentSchema:
        category = CategorySchema(
            id=payment_model.category.id,
            name=payment_model.category.name,
            subcategories=[
                SubcategorySchema(id=subcategory.id, name=subcategory.name)
                for subcategory in payment_model.category.subcategories.all()
            ])
        status = StatusSchema(id=payment_model.status.id,
                              name=payment_model.status.name)

        payment_type = TypeSchema(
            id=payment_model.payment_type.id,
            name=payment_model.payment_type.name,
            categories=[
                CategorySchema(category.id, category.name,
                               category.subcategories)
                for category in payment_model.payment_type.categories.all()
            ])
        payment = PaymentSchema(id=payment_model.id,
                                create_date=payment_model.create_date,
                                status=status,
                                payment_type=payment_type,
                                category=category,
                                subcategory=SubcategorySchema(
                                    id=payment_model.subcategory.id,
                                    name=payment_model.subcategory.name),
                                amount=payment_model.amount,
                                comment=payment_model.comment)
        return payment

    def from_query_dict_to_dto(payment: dict) -> PaymentSchema:
        dto = PaymentSchema(id=payment.get('id'),
                            create_date=payment.get('create_date'),
                            status=payment.get('status'),
                            payment_type=payment.get('payment_type'),
                            category=payment.get('category'),
                            subcategory=payment.get('subcategory'),
                            amount=payment.get('amount'),
                            comment=payment.get('comment'))
        return dto

    def filter_to_dto(filter: dict):
        return PaymentFilter(timeEnd=filter.get('timeEnd'),
                             timeStart=filter.get('timeStart'),
                             status_id=filter.get('statusId'),
                             category_id=filter.get('categoryId'),
                             subcategory_id=filter.get('subcategoryId'),
                             payment_type_id=filter.get('typeId'))
