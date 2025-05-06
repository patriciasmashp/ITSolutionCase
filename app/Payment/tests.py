from django.test import TestCase
from Directory.DirectoryService.Schemas import CategorySchema, StatusSchema, SubcategorySchema, TypeSchema
from app.Dispathcer import Dispathcer
from Directory.models import Type, Category, Subcategory, Status
from .PaymentService.Schemas import PaymentSchema


# Create your tests here.
class TestPayment(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.dispathcer: Dispathcer = Dispathcer()
        payment_type_add = Type.objects.create(name='Пополнение')
        payment_type_pay = Type.objects.create(name='Списание')

        category_infra = Category.objects.create(
            name='Инфраструктура', category_type=payment_type_pay)
        category_marketing = Category.objects.create(
            name='Маркетинг', category_type=payment_type_add)

        subcategory_vps = Subcategory.objects.create(name='VPS',
                                                     category=category_infra)
        subcategory_proxy = Subcategory.objects.create(name='Proxy',
                                                       category=category_infra)
        subcategory_farpost = Subcategory.objects.create(
            name='Farpost', category=category_marketing)
        subcategory_avito = Subcategory.objects.create(
            name='Avito', category=category_marketing)
        status_personal = Status.objects.create(name='Личное')
        status_buisnes = Status.objects.create(name='Бизнес')

        payment = {
            'payment_type': payment_type_pay.id,
            'category': category_infra.id,
            'subcategory': subcategory_vps.id,
            'status': status_buisnes.id,
            'amount': 2,
        }

        cls.dispathcer.fetch_directory_and_create_payment(payment)

    def setUp(self):
        payment_status = Status.objects.get(name='Бизнес')
        payment_type = Type.objects.get(name='Списание')
        category = Category.objects.get(name='Инфраструктура')
        subcategory = Subcategory.objects.get(name='VPS')
        amount = 2

        self.valid_payment_structure = PaymentSchema(
            status=StatusSchema(name=payment_status.name,
                                id=payment_status.id),
            category=CategorySchema(
                name=category.name,
                id=category.id,
                subcategories=category.subcategories.all()),
            subcategory=SubcategorySchema(name=subcategory.name,
                                          id=subcategory.id),
            payment_type=TypeSchema(name=category.category_type.name,
                                    categories=payment_type.categories.all(),
                                    id=category.category_type.id),
            amount=amount,
        )

    def test_create_payment(self):
        status = Status.objects.get(name='Бизнес').id
        payment_type_id = Type.objects.get(name='Списание').id
        category = Category.objects.get(name='Инфраструктура').id
        subcategory = Subcategory.objects.get(name='VPS').id
        amount = 2
        comment = 'test'
        payment = {
            'payment_type': payment_type_id,
            'category': category,
            'subcategory': subcategory,
            'status': status,
            'amount': amount,
        }
        payment_test = self.dispathcer.fetch_directory_and_create_payment(
            payment)

        self.assertEqual(self.valid_payment_structure.status.name,
                         payment_test.status.name)
        self.assertEqual(self.valid_payment_structure.category.name,
                         payment_test.category.name)
        self.assertEqual(self.valid_payment_structure.subcategory.name,
                         payment_test.subcategory.name)
        self.assertEqual(self.valid_payment_structure.payment_type.name,
                         payment_test.payment_type.name)
        self.assertEqual(self.valid_payment_structure.amount,
                         payment_test.amount)

    def test_get_payment(self):

        payment_test = self.dispathcer.get_payment(1)

        self.assertEqual(self.valid_payment_structure.status.name,
                         payment_test.status.name)
        self.assertEqual(self.valid_payment_structure.category.name,
                         payment_test.category.name)
        self.assertEqual(self.valid_payment_structure.subcategory.name,
                         payment_test.subcategory.name)
        self.assertEqual(self.valid_payment_structure.payment_type.name,
                         payment_test.payment_type.name)
        self.assertEqual(self.valid_payment_structure.amount, payment_test.amount)

    def test_wrang_type_payment(self):
        payment_type_id = Type.objects.get(name='Пополнение').id
        category = Category.objects.get(name='Инфраструктура').id
        subcategory = Subcategory.objects.get(name='VPS').id
        status = Status.objects.get(name='Бизнес').id
        amount = 2
        comment = 'test'
        payment = {
            'payment_type': payment_type_id,
            'category': category,
            'subcategory': subcategory,
            'status': status,
            'amount': amount,
        }
        with self.assertRaises(ValueError) as cm:
            self.dispathcer.fetch_directory_and_create_payment(payment)

    def test_wrang_category_payment(self):
        payment_type_id = Type.objects.get(name='Пополнение').id
        category = Category.objects.get(name='Маркетинг').id
        subcategory = Subcategory.objects.get(name='VPS').id
        status = Status.objects.get(name='Бизнес').id
        amount = 2
        comment = 'test'
        payment = {
            'payment_type': payment_type_id,
            'category': category,
            'subcategory': subcategory,
            'status': status,
            'amount': amount,
        }
        with self.assertRaises(ValueError) as cm:
            self.dispathcer.fetch_directory_and_create_payment(payment)

    def test_wrang_subcategory_payment(self):
        payment_type_id = Type.objects.get(name='Пополнение').id
        category = Category.objects.get(name='Инфраструктура').id
        subcategory = Subcategory.objects.get(name='Avito').id
        status = Status.objects.get(name='Бизнес').id
        amount = 2
        comment = 'test'
        payment = {
            'payment_type': payment_type_id,
            'category': category,
            'subcategory': subcategory,
            'status': status,
            'amount': amount,
        }
        with self.assertRaises(ValueError) as cm:
            self.dispathcer.fetch_directory_and_create_payment(payment)
