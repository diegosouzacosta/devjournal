# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serialize the model Project
    """
    class Meta:
        model = Project
        fields = (
                'id',
        )


class ProjectPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10

    class Meta:
        object_serializer_class = ProjectSerializer
