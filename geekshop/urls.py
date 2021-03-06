from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from django.urls.conf import re_path

import mainapp.views as mainapp

urlpatterns = [
    re_path(r"^$", mainapp.main, name="main"),
    re_path(r"^products/", include("mainapp.urls", namespace="products")),
    re_path(r"^contact/", mainapp.contact, name="contact"),
    re_path(r"^auth/", include("authnapp.urls", namespace="auth")),
    re_path(r"^basket/", include("basketapp.urls", namespace="basket")),
    re_path(r"^myadmin/", include("adminapp.urls", namespace="myadmin")),
    re_path(r"^admin/", admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
