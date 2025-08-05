from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path("", include("news.urls")),
    path("admin/", admin.site.urls),
]

# 开发环境下，将媒体文件路由添加到 URL 映射
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
