from django.urls import path

from . import views
from django.urls import path

urlpatterns = [
    path('extract/<str:symbol>/', views.extract, name='extract'),

]