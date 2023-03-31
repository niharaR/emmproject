from django.contrib import admin
from .models import Category,Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
  list_display=['name','slug']
  prepoplated_field={'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
  list_display=('name','slug','stock','avaiable','created','update')
  prepoplated_field={'slug':('name',)}
  list_editable = ('name',  'stock', 'avaiable')
  list_display_links = None
  list_per_page=20
admin.site.register(Product,ProductAdmin)
