# -*- coding: utf-8 -*-
# vim: ts=4 sts=4 sw=4 et:

from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination

from journal.models import Manager, Developer, Organization, Project, Milestone, Label, Issue


class ManagerSerializer(serializers.ModelSerializer):
    '''
    Serialize the model Manager
    '''
    class Meta:
        model = Manager
        fields = (
                 'name', 'email',
        )


class DeveloperSerializer(serializers.ModelSerializer):
    '''
    Serialize the model Developer
    '''
    class Meta:
        model = Developer
        fields = (
                 'name', 'email', 'avatar_url', 'github_id', 'github_login',
        )


class OrganizationSerializer(serializers.ModelSerializer):
    '''
    Serialize the model Organization
    '''
    class Meta:
        model = Organization
        fields = (
                'github_id', 'name', 'description', 'html_url', 'avatar_url',
        )


class ProjectSerializer(serializers.ModelSerializer):
    '''
    Serialize the model Projects
    '''
    class Meta:
        model = Project
        fields = (
                'id', 'github_id', 'name', 'description', 'html_url', 'created_at',
        )


class MilestoneSerializer(serializers.ModelSerializer):
    '''
    Serialize the model Milestone
    '''
    class Meta:
        model = Milestone
        fields = (
                'github_id', 'number', 'state', 'title', 'description', 'html_url', 'created_at',
                'close_at', 'update_at', 'due_on', 'project', 'creator', 'sender',
        )


class LabelSerializer(serializers.ModelSerializer):
    '''
    Serialize the model Label
    '''
    class Meta:
        model = Label
        fields = (
                'name', 'color',
        )


class IssueSerializer(serializers.ModelSerializer):
    '''
    Serialize the model Issue
    '''
    class Meta:
        model = Milestone
        fields = (
                'github_id', 'number', 'state', 'title', 'body', 'html_url', 'created_at',
                'close_at', 'update_at', 'due_on', 'project', 'milestone', 'lables', 'creator',
                'sender', 'assignee', 'closed_by'
        )


class ProjectPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10000000

    class Meta:
        object_serializer_class = ProjectSerializer
