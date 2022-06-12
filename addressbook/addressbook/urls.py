"""addressbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from address.views import add_address,get_address,update_address,delete_address
urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_address/', add_address.as_view(),name='create_address'),
    path('get_address/', get_address.as_view(),name='get_address'),
    path('update_add/<str:id>/', update_address.as_view(),name="update_add"),
    path('delete_add/<str:id>/', delete_address.as_view(),name="delete_add"),
]
