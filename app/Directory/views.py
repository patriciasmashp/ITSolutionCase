from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import View

from app.Dispathcer import Dispathcer

from .forms import CategroyForm, StatusForm, SubcategoryForm, TypeForm
from .DirectoryService.HTMLPresentator import HTMLPresentator
from .models import Category, Subcategory, Type, Status

dispather = Dispathcer()

# Типы


class CreateType(CreateView):
    model = Type
    form_class = TypeForm
    template_name = 'link_form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Создание типа'
        return context


class DeleteType(DeleteView):
    model = Type
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('directory_index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Удаление типа'
        context['enitity_name'] = 'тип: ' + context['type'].name
        return context


class EditType(UpdateView):
    model = Type
    template_name = 'link_form.html'
    form_class = TypeForm
    success_url = reverse_lazy('directory_index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Редактирование типа'
        return context


# Категория


class CreateCategory(CreateView):
    model = Category
    form_class = CategroyForm
    template_name = 'link_form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Создание категории'
        return context


class DeleteCategory(DeleteView):
    model = Category
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('directory_index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Удаление категории'
        context['enitity_name'] = 'категория: ' + context['category'].name
        return context


class EditCategory(UpdateView):
    model = Category
    template_name = 'link_form.html'
    form_class = CategroyForm
    success_url = reverse_lazy('directory_index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Редактирование категории'
        return context


# Подкатегория


class CreateSubcategory(CreateView):
    model = Subcategory
    form_class = SubcategoryForm
    template_name = 'link_form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Создание подкатегории'
        return context


class DeleteSubcategory(DeleteView):
    model = Subcategory
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('directory_index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Удаление подкатегории'
        context[
            'enitity_name'] = 'подкатегорию: ' + context['subcategory'].name
        return context


class EditSubcategory(UpdateView):
    model = Subcategory
    template_name = 'link_form.html'
    form_class = SubcategoryForm
    success_url = reverse_lazy('directory_index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Редактирование подкатегории'
        return context


# Статус


class CreateStatus(CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'link_form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Создание статуса'
        return context


class DeleteStatus(DeleteView):
    model = Status
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('directory_index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Удаление статуса'
        context['enitity_name'] = 'статус: ' + context['status'].name
        return context


class EditStatus(UpdateView):
    model = Status
    template_name = 'link_form.html'
    form_class = StatusForm
    success_url = reverse_lazy('directory_index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Редактирование статуса'
        return context


class DirectoryView(View):

    def get(self, request):
        types = dispather.get_types()
        statuses = dispather.get_statuses()
        categories = dispather.get_categories()
        subcategories = dispather.get_subcategories()

        return render(request,
                      'list_view.html',
                      context={
                          "types":
                          HTMLPresentator.type_list(types),
                          "statuses":
                          HTMLPresentator.status_list(statuses),
                          "categories":
                          HTMLPresentator.category_list(categories),
                          "subcategories":
                          HTMLPresentator.subcategory_list(subcategories)
                      })
