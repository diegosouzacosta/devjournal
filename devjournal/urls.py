from django.conf.urls import include, url
from django.contrib import admin

from journal import urls as journal_url


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^journal/', include(journal_url)),
]
