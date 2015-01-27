from django.contrib import admin

# Register your models here.

from products.models import Product,ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3

class ProductAdmin(admin.ModelAdmin):
	inlines = [ProductImageInline]
	list_display = ('product_title','product_price','product_pub_date')
	list_filter = ['product_pub_date']
	search_fields = ['product_title']
	fieldsets = [
	    (None, {'fields': ['product_title','product_price','product_description']}),
	    ('Date information', {'fields': ['product_pub_date']}),
    ]
    

admin.site.register(Product, ProductAdmin)
