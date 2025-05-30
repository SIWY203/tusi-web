from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from filebrowser.sites import site
from django.conf import settings

admin.site.site_header = "Panel administracyjny TUSI"
admin.site.site_title = "TUSI Admin"
admin.site.index_title = "Zarządzanie stroną"

urlpatterns = [
    path("admin/filebrowser/", site.urls),
    path('admin/', admin.site.urls),
    path('', include('tusi.urls')),
]

# media folder
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
