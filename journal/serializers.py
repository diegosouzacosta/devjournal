# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination

from journal.models import Projects


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serialize the model Projects
    """
    class Meta:
        model = Projects
        fields = (
                'id', 'github_id', 'name', 'description', 'html_url', 'created_at',
        )


class ProjectPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10000000

    class Meta:
        object_serializer_class = ProjectSerializer
