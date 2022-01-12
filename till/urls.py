from django.urls import path
from . import views

urlpatterns = [
    path('', views.till, name='till'),
    path('till_success/<order_number>', views.till_success, name='till_success'),
]