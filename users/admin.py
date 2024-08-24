from django.contrib import admin

from users.models import User


@admin.register(User)
class RetailChainAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
    )
