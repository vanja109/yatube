from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('posts.urls', namespace='posts')),
    path('auth/', include('users.urls')),
    path('about/', include('about.urls', namespace='about')),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
]

handler500 = 'core.views.server_error'
handler403 = 'core.views.permission_denied'
handler404 = 'core.views.page_not_found'

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)

    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
