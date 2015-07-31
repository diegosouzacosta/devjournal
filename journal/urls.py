# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from journal.views import JournalDailyViewSet, JournalWeeklyViewSet


urlpatterns = patterns(
    'journal.views',
    url(r'^daily/$', JournalDailyViewSet.as_view(), name='daily'),
    url(r'^weekly/$', JournalWeeklyViewSet.as_view(), name='weekly'),
)
