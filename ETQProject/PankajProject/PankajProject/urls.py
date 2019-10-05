from django.contrib import admin
from django.urls import path,include
from PankajApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showRegistrationPage),
    path('loginbtn/', views.validateUser),
    path('okbtn/', views.pageUser),
    path('home/',views.homeView, name='home'),
    path('user/', views.userView, name='user'),
    path('mapping/', views.mappingView, name='map'),
    path('etq/',views.etqView, name='etq'),
    path('scheduler/', views.schedulerView, name='scheduler'),
    path('batch/',views.batchView, name='batch'),
    #path('user/<int:pk>', views.userView, name='user_detail'),
    #path('user/', include('django.contrib.auth.urls')),
]
