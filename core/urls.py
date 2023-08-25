from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('projects/', include('portfolio.urls', namespace='projects')),
    path('api/', include('blog_api.urls', namespace='blog_api')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)