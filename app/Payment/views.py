import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.http.request import HttpRequest
from django.core.exceptions import ValidationError
from django.views import View
from django.template.loader import render_to_string
from Payment.PaymentService.HTMLPresentator import HTMLPresentator
from Directory.DirectoryService.HTMLPresentator import HTMLPresentator as DirectoryHTMLPresentator
from app.Dispathcer import Dispathcer
from .Forms import (PaymentForm, PaymentTypeForm, CategoryForm, StatusForm,
                    SubCategoryForm, AmountForm, CommentForm, SuccessForm)

dispathcer = Dispathcer()


class IndexView(View):

    def get(self, request, *args, **kwargs):
        """
        Индексная страница
        """
        payments = dispathcer.get_payments()
        types = dispathcer.get_types()
        categories = dispathcer.get_categories()
        subcategories = dispathcer.get_subcategories()
        statuses = dispathcer.get_statuses()
        return render(
            request,
            'index.html',
            context={
                'payments':
                HTMLPresentator.payment_list(payments),
                'form':
                PaymentTypeForm(),
                'categories':
                DirectoryHTMLPresentator.category_list(categories),
                'subcategories':
                DirectoryHTMLPresentator.subcategory_list(subcategories),
                'statuses':
                DirectoryHTMLPresentator.status_list(statuses),
                'types':
                DirectoryHTMLPresentator.type_list(types),
            })

    def delete(self, payment_id: int):
        """Удаление платежа"""

        result = dispathcer.delete_payment(payment_id)

        return JsonResponse({'success': result})

    def post(self, request: HttpRequest, *args, **kwargs):
        """Добавление платежа"""
        # Формируем данные из связанного списка
        data = json.loads(request.body)
        del data['filled']
        # Создаем платеж
        payment_created = dispathcer.fetch_directory_and_create_payment(data)

        return render(
            request=request,
            template_name='TableRow.html',
            context={'payment': HTMLPresentator.payment(payment_created)})


def edit_payment(request: HttpRequest, payment_id: int):
    """Редактирование платежа"""
    if request.POST:
        form = PaymentForm(data=request.POST)
        try:
            # Пытаемся обновить платеж
            payment_updated = dispathcer.fetch_directory_and_update_payment(
                form.data.dict())
        except ValueError as e:
            # В случае ошибки добавляем ошибку в форму и отправляем

            form.add_error(None, ValidationError(e.args[0]))
        print(form.errors)
        if form.errors:
            return HttpResponse(form.non_field_errors().render(), status=400)
        return render(
            request=request,
            template_name='TableRow.html',
            context={'payment': HTMLPresentator.payment(payment_updated)})


def getPaymentForm(request: HttpRequest, payment_id: int):
    """Ручка для получения формы редактирования платежа"""
    payment = dispathcer.get_payment(payment_id)

    return HttpResponse(PaymentForm(payment).render())


def handleForm(request: HttpRequest):
    """Ручка для обработки формы"""

    # Задаем порядок ввода данных
    orderInputs = {
        'payment_type': PaymentTypeForm,
        'status': StatusForm,
        'category': CategoryForm,
        'subcategory': SubCategoryForm,
        'amount': AmountForm,
    }

    # Формируем данные для формы из связаного списка
    formData = {}
    data = json.loads(request.body)

    formData[data['name']] = data['value']
    if data['value'] != '':
        while data['next'] is not None:

            formData[data['next']['name']] = data['next']['value']
            data = data['next']

    # Получаем следующий элемент формы
    next_index = list(orderInputs.keys()).index(data['name']) + 1
    if next_index >= len(orderInputs):
        return JsonResponse({
            'filled': 'filled',
            'comment': CommentForm(formData).render()
        })
    next_key = list(orderInputs.keys())[next_index]

    nextElem = orderInputs.get(next_key)
    # Передаем на фронт элемент с данными
    return HttpResponse(nextElem(formData))


def filterPayments(request: HttpRequest):
    """Ручка для фильтрации платежей"""
    data = json.loads(request.body)

    payments = dispathcer.filter_payments(data)
    table_rows = [
        render_to_string('TableRow.html', {'payment': payment})
        for payment in HTMLPresentator.payment_list(payments)
    ]

    return JsonResponse({"payments": table_rows})
