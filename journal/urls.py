# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from journal.views import JournalDailyViewSet


urlpatterns = patterns(
    'journal.views',
    url(r'^daily/$', JournalDailyViewSet.as_view(), name='daily'),
)
