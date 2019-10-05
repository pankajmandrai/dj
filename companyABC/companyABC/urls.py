"""companyABC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from empMast import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showRegistrationPage),
    path('loginbtn/', views.validateUser),
    path('okbtn/', views.pageUser),
    path('home/',views.homeView, name='home'),
    path('user/', views.userView, name='user'),
    path('mapping/', views.mappingView, name='map'),
    path('etq/',views.employeView, name='etq'),
    path('scheduler/', views.schedulerView, name='scheduler'),
    path('batch/',views.batchView, name='batch'),
    #path('user/<int:pk>', views.userView, name='user_detail'),
    #path('user/', include('django.contrib.auth.urls')),
]

