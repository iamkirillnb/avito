from django.contrib import admin
from .models import Search

class SearchAdmin(admin.ModelAdmin):
    list_display = ('id', 'link', 'region', )
    list_display_links = ('link',)

admin.site.register(Search, SearchAdmin)