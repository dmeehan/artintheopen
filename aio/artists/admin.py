# artists/admin.py

from django.contrib import admin
from django.conf import settings
from .models import *
    
    
class ArtistOptions(admin.ModelAdmin):

    #def photo(self):
    #    if self.photo:
    #        return '<img src="%s" />' % self.photo.url_thumbnail
    #    else:
    #        return ""
    #photo.allow_tags = True
    
    list_display = ('last_name', 'first_name', 'status', 'featured_home', 'featured_artists',)
    prepopulated_fields = {'slug': ('first_name','last_name',)}
    fieldsets = (
        (None, {
            'fields': ('user',)
        }),
        ('Professional Information', {
            'fields': ('first_name', 'last_name', 'bio', 'website', 'photo', 'image',)
        }),
        ('Contact Information', {
            'classes': ('collapse-open',),
            'fields' : ('address', 'city', 'state', 'zip_code', 'phone'),
        }),
        ('Display Options', {
            'classes': ('collapse-open',),
            'fields': ('status', 'featured_home', 'featured_artists', 'slug',)
        }),
        ('Festival Information', {
            'classes': ('collapse-closed',),
            'fields': ('location',)
        }),
    )
    
    
    
    # Media
    class Media:
        js = [
            settings.STATIC_URL + 'tinymce/jscripts/tiny_mce/tiny_mce.js',
            settings.STATIC_URL + 'tinymce_setup/tinymce_setup.js',
        ]

admin.site.register(Artist, ArtistOptions)
