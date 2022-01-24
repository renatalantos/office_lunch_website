"""
Urls fo tills app.
"""
from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.till, name='till'),
    path('till_success/<order_number>',
         views.till_success,
         name='till_success'),
    path('cache_till_data/', views.cache_till_data, name='cache_till_data'),
    path('wh/', webhook, name='webhook'),
]
