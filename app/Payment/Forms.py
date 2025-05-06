from django import forms
from django.core.exceptions import ValidationError
from Payment.PaymentService.Schemas import PaymentSchema
from Payment.models import Payment
from app.Dispathcer import Dispathcer
from Directory.models import Status, Type, Category, Subcategory
from app.Mappers.DjangoPaymentMapper import DjangoPaymentMapper

dispathcer = Dispathcer()


class PaymentForm(forms.Form):

    class Meta:
        model = Payment
        fields = '__all__'

    def __init__(self, payment: PaymentSchema = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'] = forms.IntegerField(
            initial=payment.id if payment else '',
            widget=forms.HiddenInput({'id': 'id'}))
        self.fields['payment_type'] = forms.ModelChoiceField(
            widget=forms.Select(attrs={'class': 'form-select my-2'}),
            label='',
            initial=payment.payment_type.id if payment else '',
            empty_label='Тип',
            queryset=Type.objects.all())
        self.fields['category'] = forms.ModelChoiceField(
            widget=forms.Select(attrs={'class': 'form-select my-2'}),
            empty_label='Категория',
            label='',
            initial=payment.category.id if payment else '',
            queryset=Category.objects.all())
        self.fields['subcategory'] = forms.ModelChoiceField(
            widget=forms.Select(attrs={'class': 'form-select my-2'}),
            empty_label='Подкатегория',
            label='',
            initial=payment.subcategory.id if payment else '',
            queryset=Subcategory.objects.all())
        self.fields['status'] = forms.ModelChoiceField(
            queryset=Status.objects.all(),
            initial=payment.status.id if payment else '',
            empty_label='Статус',
            label='',
            widget=forms.Select(attrs={'class': 'form-select my-2'}))
        self.fields['amount'] = forms.IntegerField(
            min_value=0,
            initial=payment.amount if payment else '',
            label='',
            widget=forms.NumberInput(attrs={
                'class': 'form-control my-2',
                'placeholder': 'Сумма'
            }))
        self.fields['comment'] = forms.CharField(
            initial=payment.comment if payment else '',
            label='',
            required=False,
            widget=forms.Textarea(attrs={
                'class': 'form-control my-2',
                'placeholder': 'Комментарий'
            }))

    def clean(self):
        super().clean()


class PaymentTypeForm(forms.Form):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

    payment_type = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'form-select my-2'}),
        empty_label='Тип',
        queryset=Type.objects.all())


class CategoryForm(forms.Form):

    def __init__(self, data: dict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = data
        self.queryset = Type.objects.get(
            id=data['payment_type']).categories.all()
        self.fields['category'] = forms.ModelChoiceField(
            widget=forms.Select(attrs={'class': 'form-select my-2'}),
            empty_label='Категория',
            queryset=self.queryset)


class SubCategoryForm(forms.Form):

    def __init__(self, data: dict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = data
        self.queryset = Category.objects.get(
            id=data['category']).subcategories.all()
        self.fields['subcategory'] = forms.ModelChoiceField(
            widget=forms.Select(attrs={'class': 'form-select my-2'}),
            empty_label='Подкатегория',
            queryset=self.queryset)


class StatusForm(forms.Form):

    def __init__(self, data: dict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = data

        self.queryset = Status.objects.all()
        self.fields['status'] = forms.ModelChoiceField(
            queryset=self.queryset,
            empty_label='Статус',
            widget=forms.Select(attrs={'class': 'form-select my-2'}))


class AmountForm(forms.Form):

    def __init__(self, data: dict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = data

        self.fields['amount'] = forms.IntegerField(
            min_value=0,
            widget=forms.NumberInput(attrs={
                'class': 'form-control my-2',
                'placeholder': 'Сумма'
            }))


class CommentForm(forms.Form):

    def __init__(self, data: dict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = data

        self.fields['comment'] = forms.CharField(
            label='',
            widget=forms.Textarea(attrs={
                'class': 'form-control my-2',
                'placeholder': 'Комментарий'
            }))


class SuccessForm():

    def __init__(self, data: dict, *args, **kwargs):

        self.data = data

    def __call__(self, *args, **kwds):

        return 'filled'
