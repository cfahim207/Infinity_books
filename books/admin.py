from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',),}
    
class BooksAdmin(admin.ModelAdmin):
    list_display=['title','writer','published']
    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Books,BooksAdmin)
admin.site.register(Review)