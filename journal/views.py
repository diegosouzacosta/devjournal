# -*- coding: utf-8 -*-
# vim: ts=4 sts=4 sw=4 et:

import logging

import dateutil.parser
from datetime import datetime
from rest_framework import generics

from journal.models import Developer
from journal.serializers import DeveloperSerializer
from journal.serializers import DeveloperPagination


log = logging.getLogger(__name__)


def get_date_start_end(params):
    '''
    Pass the end date and initial date values received in the initial url to datetime
    '''
    date_start = params.get('date-start', None)
    if date_start:
        date_start = dateutil.parser.parse(date_start)
    else:
        date_start = datetime.now()

    date_end = params.get('date-end', None)
    if date_end:
        date_end = dateutil.parser.parse(date_end)
    else:
        date_end = datetime.now()

    return date_start, date_end


class JournalDailyViewSet(generics.ListAPIView):
    '''
    - View that returns the query to the model Projec. Send in JSON format
    '''
    # disable interface of django-rest-framework
    # renderer_classes = [renderers.JSONRenderer]

    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    pagination_class = DeveloperPagination
    model = Developer

    def get_queryset(self):
        '''
        bla bla bla
        '''
        date_start, date_end = get_date_start_end(self.request.query_params)
        organization = self.request.query_params.get('organization', None)
        print ('@----------------@')
        print (date_start)
        print (date_end)
        print (organization)
        return Developer.objects.get_values(date_start, date_end, organization)
