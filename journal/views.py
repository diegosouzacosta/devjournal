# -*- coding: utf-8 -*-

from rest_framework import generics

import logging
from journal.models import Projects
from journal.serializers import ProjectSerializer
from journal.serializers import ProjectPagination


log = logging.getLogger(__name__)


class JournalViewSet(generics.ListAPIView):
    '''
    - View that returns the query to the model Projec. Send in JSON format
    '''
    # disable interface of django-rest-framework
    # renderer_classes = [renderers.JSONRenderer]

    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectPagination
    model = Projects
