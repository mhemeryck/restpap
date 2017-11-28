from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers


router = routers.DefaultRouter()

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'', include(router.urls)),
]
