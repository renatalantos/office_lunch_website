from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.till, name='till'),
    path('till_success/<order_number>', views.till_success, name='till_success'),
    path('wh/', webhook, name='webhook'),
]