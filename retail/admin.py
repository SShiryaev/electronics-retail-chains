from django.contrib import admin

from retail.models import RetailChain, Product


@admin.action(description='Убрать задолженность перед поставщиком')
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0.00)


@admin.register(RetailChain)
class RetailChainAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'country',
        'city',
        'chain_level',
        'supplier',
        'debt',
        'created_at',
    )
    list_filter = ('city',)
    search_fields = ('name',)
    actions = [clear_debt]
    list_display_links = ['supplier']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'product_model',
        'release_date',
        'retail_chain',
    )
    list_filter = ('retail_chain',)
    search_fields = ('name',)
    list_display_links = ['retail_chain']
