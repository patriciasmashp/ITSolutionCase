from django import forms

from .models import Category, Type, Subcategory, Status


class CategroyForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'category_type']

    name = forms.CharField(max_length=100,
                           label='',
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Название'
                           }))

    category_type = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        label='',
        empty_label='Тип',
        widget=forms.Select(attrs={'class': 'form-control'}))


class SubcategoryForm(forms.ModelForm):

    class Meta:
        model = Subcategory
        fields = ['name', 'category']

    name = forms.CharField(max_length=100,
                           label='',
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Название'
                           }))

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='',
        empty_label='Категория',
        widget=forms.Select(attrs={'class': 'form-control'}))


class TypeForm(forms.ModelForm):

    class Meta:
        model = Type
        fields = ['name']

    name = forms.CharField(max_length=100,
                           label='',
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Название'
                           }))


class StatusForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = ['name']

    name = forms.CharField(max_length=100,
                           label='',
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Название'
                           }))
