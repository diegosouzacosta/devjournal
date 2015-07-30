# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from journal.views import JournalViewSet


urlpatterns = patterns(
    'journal.views',
    url(r'^all/$', JournalViewSet.as_view()),
)
