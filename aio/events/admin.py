# events/admin.py

from django.contrib import admin
from django.conf import settings
from .models import *
    
    
class EventOptions(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'host')
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        (None, {
            'fields': ('title', 'start_date', 'end_date', 'start_time', 'end_time', 'aio', 'affiliate', 'host', 'fee', 'description', 'image',)
        }),
        ('Location Information', {
            'classes': ('collapse-open',),
            'fields' : ('location_name', 'address', 'city', 'state', 'zip_code', 'location',),
        }),
        ('Contact Information', {
            'classes': ('collapse-open',),
            'fields' : ('contact', 'phone', 'email', 'website',),
        }),
        ('Display Options', {
            'classes': ('collapse-open',),
            'fields': ('featured_home', 'featured_events', 'slug',)
        }),
    )
    
    # Media
    class Media:
        js = [
            settings.STATIC_URL + 'tinymce/jscripts/tiny_mce/tiny_mce.js',
            settings.STATIC_URL + 'tinymce_setup/tinymce_setup.js',
        ]

admin.site.register(Event, EventOptions)
