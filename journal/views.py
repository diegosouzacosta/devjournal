# -*- coding: utf-8 -*-
# vim: ts=4 sts=4 sw=4 et:

import logging

import dateutil.parser
from datetime import datetime, timedelta
from rest_framework import generics

from journal.models import Developer, Project
from journal.serializers import DeveloperSerializer, ProjectWeeklySerializer
from journal.serializers import DeveloperPagination, ProjectWeeklyPagination


log = logging.getLogger(__name__)


def get_date_start_end(params):
    '''
    Pass the end date and initial date values received in the initial url to datetime
    '''
    date_start = params.get('date-start', None)
    if date_start:
        date_start = dateutil.parser.parse(date_start)
    else:
        date_start = datetime.today()

    date_end = params.get('date-end', None)
    if date_end:
        date_end = dateutil.parser.parse(date_end) + timedelta(1)
    else:
        date_end = datetime.today() + timedelta(1)

    return date_start, date_end


class JournalDailyViewSet(generics.ListAPIView):
    '''
    - View that returns the query to the model Developer. Send in JSON format
    '''
    # disable interface of django-rest-framework
    # renderer_classes = [renderers.JSONRenderer]

    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    pagination_class = DeveloperPagination
    model = Developer

    def get_queryset(self):
        '''
        Filter values for the url
        '''
        date_start, date_end = get_date_start_end(self.request.query_params)
        organization = self.request.query_params.get('organization', None)
        return Developer.objects.get_values_daily(date_start, date_end, organization)


class JournalWeeklyViewSet(generics.ListAPIView):
    '''
    - View that returns the query to the model Project. Send in JSON format
    '''
    # disable interface of django-rest-framework
    # renderer_classes = [renderers.JSONRenderer]

    queryset = Project.objects.all()
    serializer_class = ProjectWeeklySerializer
    pagination_class = ProjectWeeklyPagination
    model = Project

    def get_queryset(self):
        '''
        Filter values for the url
        '''
        date_start, date_end = get_date_start_end(self.request.query_params)
        organization = self.request.query_params.get('organization', None)
        return Project.objects.get_values_weekly(date_start, date_end, organization)
