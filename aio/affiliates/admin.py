# affiliates/admin.py

from django.contrib import admin
from django.conf import settings
from .models import *
    
    
class AffiliateOptions(admin.ModelAdmin):
    list_display = ('name', 'affiliate_level', 'featured_home', 'featured_affiliates')
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = (
        (None, {
            'fields': ('affiliate_type', 'name', 'affiliate_level', 'website', 'image',)
        }),
        ('Display Options', {
            'classes': ('collapse-open',),
            'fields': ('featured_home', 'featured_affiliates', 'slug',)
        }),
    )
    
    # Media
    class Media:
        js = [
            settings.STATIC_URL + 'tinymce/jscripts/tiny_mce/tiny_mce.js',
            settings.STATIC_URL + 'tinymce_setup/tinymce_setup.js',
        ]

admin.site.register(Affiliate, AffiliateOptions)
admin.site.register(AffiliateLevel)
