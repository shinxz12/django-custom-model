from django.contrib import admin
from .models import Book, Category, Discount

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    pass

class BookAdmin(admin.ModelAdmin):
    pass

class DiscountAdmin(admin.ModelAdmin):
    pass

register_list = (
    (Book, BookAdmin, ),
    (Category, CategoryAdmin, ),
    (Discount, DiscountAdmin, ),
)
for register_item in register_list:
    admin.site.register(*register_item)
admin.site.enable_nav_sidebar = False
