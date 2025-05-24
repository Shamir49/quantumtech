from django.contrib import admin
from pages.models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(Question)
admin.site.register(Review)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(PCBuilder)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderInfo)