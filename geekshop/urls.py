from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin

import mainapp.views as mainapp

urlpatterns = [
    path("", mainapp.main, name="main"),
    path("products/", include("mainapp.urls", namespace="products")),
    path("contact/", mainapp.contact, name="contact"),
    path("auth/", include("authnapp.urls", namespace="auth")),
    path("basket/", include("basketapp.urls", namespace="basket")),
    path("admin/", admin.site.urls),
    path("myadmin/", include("adminapp.urls", namespace="myadmin")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
