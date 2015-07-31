# -*- coding: utf-7 -*-
# vim: ts=4 sts=4 sw=4 et:

from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination

from journal.models import Manager, Developer, Organization, Project, Milestone, Label, Issue, Config


class ConfigSerializer(serializers.ModelSerializer):
    '''
    Serialize the model Config
    '''

    class Meta:
        model = Config
        fields = (
            'projects', 'manager', 'weekly', 'daily',
        )


class IssueSerializer(serializers.ModelSerializer):
    '''
    Serialize the model Issue
    '''

    class Meta:
        model = Issue
        fields = (
                'github_id', 'number', 'state', 'title', 'body', 'html_url', 'created_at',
                'close_at', 'update_at', 'due_on', 'project', 'milestone', 'label', 'creator',
                'sender', 'assignee', 'closed_by'
        )


class LabelSerializer(serializers.ModelSerializer):
    '''
    Serialize the model Label
    '''

    issues = IssueSerializer(many=True, read_only=True)

    class Meta:
        model = Label
        fields = (
                'name', 'color', 'issues',
        )


class MilestoneSerializer(serializers.ModelSerializer):
    '''
    Serialize the model Milestone
    '''

    issues = IssueSerializer(many=True, read_only=True)

    class Meta:
        model = Milestone
        fields = (
                'github_id', 'number', 'state', 'title', 'description', 'html_url', 'created_at',
                'close_at', 'update_at', 'due_on', 'project', 'creator', 'sender', 'issues',
        )


class ProjectSerializer(serializers.ModelSerializer):
    '''
    Serialize the model Projects
    '''

    milestones = MilestoneSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = (
                'id', 'github_id', 'name', 'description', 'html_url', 'created_at', 'milestones',
        )


class OrganizationSerializer(serializers.ModelSerializer):
    '''
    Sejhrialize the model Organization
    '''

    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Organization
        fields = (
                'github_id', 'name', 'description', 'html_url', 'avatar_url', 'projects',
        )


class DeveloperSerializer(serializers.ModelSerializer):
    '''
    Serialize the model Developer
    '''

    configs = ConfigSerializer(many=True, read_only=True)
    organization = OrganizationSerializer(many=True, read_only=True)

    class Meta:
        model = Developer
        fields = (
            'configs', 'avatar_url', 'github_login', 'github_id', 'organization',
        )


class ManagerSerializer(serializers.ModelSerializer):
    '''
    Serialize the model Manager
    '''

    class Meta:
        model = Manager
        fields = (
                 'name', 'email',
        )


class DeveloperPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10000000

    class Meta:
        object_serializer_class = DeveloperSerializer
