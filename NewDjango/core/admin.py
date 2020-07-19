from django.contrib import admin
from .models import Item, OrderItem, Order, Review, OrderedList


admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Review)
admin.site.register(OrderedList)

