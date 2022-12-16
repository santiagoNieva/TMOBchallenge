import io
from django.contrib import admin
from django.core.cache import cache
from django.core.management import call_command
from django.http import HttpResponseRedirect
from django.urls import path
from django.utils.safestring import mark_safe
from .models import Redirect
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

    search_fields = [
        'key',
        'url'
    ]

    def cached(self, obj):
        return True if cache.get(obj.key) else False
    cached.short_description = "Cached"
    cached.boolean = True

    change_list_template = "Redirection/restore_cache.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('restore_cache/', self.restore_cache),
        ]
        return my_urls + urls

    def restore_cache(self, request):
        with io.StringIO() as out:
            call_command('restore_cache', stdout=out)
            nocolor = out.getvalue().replace("[0m", "<br>")
            nocolor = nocolor.replace("[32;1m", "")
            self.message_user(request, mark_safe(f"<b>{nocolor}</b>"))
        return HttpResponseRedirect("../")
                    
                    

