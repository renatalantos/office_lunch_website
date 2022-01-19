from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_favourite_list, name='favourites'),
    path('add/<int:item_id>/', views.add_product_to_favourites, name='add_to_favourites'),
    path('delete/<int:item_id><redirect_from>/', views.remove_product_from_favourites, name='remove_from_favourites'),
]