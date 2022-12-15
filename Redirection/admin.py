from django.contrib import admin
from .models import Redirect
from django.core.cache import cache
# Register your models here.

@admin.register(Redirect)
class RedirectAdmin(admin.ModelAdmin):
    list_display = (
        'key',
        'url',
        'active',
        'updated_at',
        'created_at',
        'cached'
    )

    list_filter = (
        'active',
    )

    search_fields= [
        'key',
        'url'
    ]

    def cached(self,obj):
        return True if cache.get(obj.key) else False
    cached.short_description = "Cached"
    cached.boolean = True