from django.conf import settings
from django.conf.urls import include, url
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#from aio import admin as aioAdmin
from filebrowser.sites import site
admin.autodiscover()



urlpatterns = [
    # Example:
    # (r'^myproject/', include('myproject.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Filebrowser. Must go before admin
    url(r'^admin/filebrowser/', include(site.urls)),
    
    # Grappelli admin extension
    url(r'^grappelli/', include('grappelli.urls')),

    # tinymce admin extension
    url(r'^tinymce/', include('tinymce.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # user authentication
    url('^accounts/', include('django.contrib.auth.urls')),
    #url(r'^accounts/login/$', auth_views.login),
    #url(r'^accounts/login/$', 'django.contrib.auth.views.login', name="login"),
    #url(r'^accounts/login/(?P<next_page>.*)/$', 'django.contrib.auth.views.login', name='login_next'),
    #url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout"),
    url(r'^$', include('home.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^artists/', include('artists.urls')),
    url(r'^affiliates/', include('affiliates.urls')),
    url(r'^events/', include('events.urls')),
    
    # Redirects
    url(r'^call_for_artists.html', RedirectView.as_view(url='/artists/call-artists/')),
    url(r'^index.html', RedirectView.as_view(url='/')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
