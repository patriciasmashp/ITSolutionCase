"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from Directory.views import (DirectoryView,
                             CreateStatus, EditStatus, DeleteStatus,
                             CreateSubcategory, EditSubcategory, DeleteSubcategory,
                             CreateCategory, EditCategory, DeleteCategory,
                             CreateType, EditType, DeleteType)

from django.conf.global_settings import DEBUG

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import Payment.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("delete/<int:payment_id>",
         Payment.views.IndexView.as_view(),
         name='delete_payment'),
    path("", Payment.views.IndexView.as_view(), name='index'),
    path("<int:payment_id>", Payment.views.edit_payment, name='update'),
    path("getPayment/<int:payment_id>",
         Payment.views.getPaymentForm,
         name='get_payment'),
    path("sendForm", Payment.views.handleForm, name='handle_form'),
    path("filter", Payment.views.filterPayments, name='filter'),
    # DIRECTORY URLS

    path("create_status", CreateStatus.as_view(), name='create_status'),
    path("delete_status/<int:pk>", DeleteStatus.as_view(), name='delete_status'),
    path("edit_status/<int:pk>", EditStatus.as_view(), name='edit_status'),

    path("create_type",
         CreateType.as_view(),
         name='create_type'),
    path("edit_type/<int:pk>",
         EditType.as_view(),
         name='edit_type'),
    path("delete_type/<int:pk>",
         DeleteType.as_view(),
         name='delete_type'),

    path("create_subcategory",
         CreateSubcategory.as_view(),
         name='create_subcategory'),
    path("edit_subcategory/<int:pk>",
         EditSubcategory.as_view(),
         name='edit_subcategory'),
    path("delete_subcategory/<int:pk>",
         DeleteSubcategory.as_view(),
         name='delete_subcategory'),
    
    path("create_category",
         CreateCategory.as_view(),
         name='create_category'),
    path("edit_category/<int:pk>",
         EditCategory.as_view(),
         name='edit_category'),
    path("delete_category/<int:pk>",
         DeleteCategory.as_view(),
         name='delete_category'),
    
    path("dirs", DirectoryView.as_view(), name='directory_index'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) if DEBUG else []
