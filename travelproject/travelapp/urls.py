from . import views
from django.urls import path

urlpatterns = [
    path('', views.demo, name='demo'),
    # path('vals/', views.values, name='values')
    ]