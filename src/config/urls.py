# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

#from accounts.views import (login_view, register_view, logout_view)

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    #url(r'^api/v1/accounts/', include("accounts.api.v1.urls", namespace='accounts-api')),
    #url(r'^docs/', include('rest_framework_docs.urls')),
    # url(r'^posts/$', "<appname>.views.<function_name>"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)