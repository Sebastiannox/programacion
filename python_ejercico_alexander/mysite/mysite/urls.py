"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
#from crudapp import views
from tutorial import views
from tutorial.views import PersonListView
from agenda.views import IndexView

urlpatterns = [
    path('', PersonListView.as_view(), name='index'),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('people/', PersonListView.as_view(), name='index'),
    path('usuarios/<int:pk>/', views.UsuarioDetailView.as_view(), name='detail'),
    path('usuarios/edit/<int:pk>', views.edit, name='edit'),
    path('usuario/create/', views.create, name="create"),
    path('usuarios/delete/<int:pk>/', views.delete, name='delete'),
    path("agenda/", IndexView.as_view())
]
