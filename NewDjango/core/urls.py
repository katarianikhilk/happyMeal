from django.urls import path
# from .views import(
#         menu,
#         ItemListView,
#         ItemCreateView,
#         add_to_cart,
#         remove_from_cart,
#         remove_single_item_from_cart,
#         OrderSummaryView,
#         filterItems,
#         search,
#         add_review,
#         edit_review,
#         delete_review,
#         detail,
#     )
from .views import *
from . import views

app_name = 'core'

urlpatterns = [
    path('menu/', menu , name='menu'),
    path('filter/', filterItems, name='filter'),
    path('search/', search, name='search'),
    path('chef-item-list/', chefItemList , name='chef-item-list'),
    # path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('product/<slug>', detail, name='product'),
    # path('item/new/', ItemCreateView.as_view(), name='product-create'),
    path('item/new/', create_item, name='product-create'),
    path('chef-list/',chef_list, name='chef-list'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
     path('order-history/', OrderHistoryView.as_view(), name='order-history'),
    path('ordered-food-list/', OrderedFoodListView.as_view(), name='ordered-food-list'),
    path('add-to-cart/<slug>/',add_to_cart, name='add-to-cart'),
    path('set-item-unavailable/<slug>/',set_item_unavailable, name='set-item-unavailable'),
    path('set-item-available/<slug>/',set_item_available, name='set-item-available'),
    path('item_delivered/<slug>/<chef_key>',item_delivered, name='item-delivered'),
    path('item_cooking/<slug>/<chef_key>',item_cooking, name='item-cooking'),
    path('remove-from-cart/<slug>/',remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/',remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('addreview/<slug>/', views.add_review, name='add_review'),
    path('edit_review/<slug>/<review_id>',views.edit_review, name='edit_review'),
    path('delete_review/<slug>/<review_id>',views.delete_review, name='delete_review'),
    path('edit_item/<slug>',views.edit_item, name='edit_item'),
]