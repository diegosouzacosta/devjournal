# -*- coding: utf-8 -*-
# vim: ts=4 sts=4 sw=4 et:

from rest_framework import generics

import logging
from journal.models import Project
from journal.serializers import ProjectSerializer
from journal.serializers import ProjectPagination


log = logging.getLogger(__name__)


class JournalViewSet(generics.ListAPIView):
    '''
    - View that returns the query to the model Projec. Send in JSON format
    '''
    # disable interface of django-rest-framework
    # renderer_classes = [renderers.JSONRenderer]

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectPagination
    model = Project
