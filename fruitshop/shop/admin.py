from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Ctegory,Subcategory,Product,ProductImg,ProductVidio

class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 0

class ProductImageInline(admin.TabularInline):
    model = ProductImg
    extra = 0

class ProductVidioInline(admin.TabularInline):
    model = ProductVidio
    extra = 0

@admin.register(Ctegory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    inlines = [
        SubcategoryInline
    ]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','quantity','weight','category')
    list_display_links = ('name',)
    list_editable = ('price','quantity','weight','category')
    inlines = [
        ProductImageInline,
        ProductVidioInline
    ]
    def get_image(self, product):
        images = product.productimg_set.all()
        if images:
            return mark_safe(f'<img scr="{images[0].image.url}" width="100">')
        return '-'


