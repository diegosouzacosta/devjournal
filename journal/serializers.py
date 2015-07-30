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
                'close_at', 'update_at', 'due_on', 'project', 'milestone', 'labels', 'creator',
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
    issues = IssueSerializer(many=True, read_only=True)
    configs = ConfigSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = (
                'id', 'github_id', 'name', 'description', 'html_url', 'created_at', 'milestones', 'issues', 'configs',
        )


class DeveloperSerializer(serializers.ModelSerializer):
    '''
    Serialize the model Developer
    '''

    projects = ProjectSerializer(many=True, read_only=True)
    creator_milestones = MilestoneSerializer(many=True, read_only=True)
    sender_milestones = MilestoneSerializer(many=True, read_only=True)
    creator_issues = IssueSerializer(many=True, read_only=True)
    sender_issues = IssueSerializer(many=True, read_only=True)
    assignee_issues = IssueSerializer(many=True, read_only=True)
    closedby_issues = IssueSerializer(many=True, read_only=True)

    class Meta:
        model = Developer
        fields = (
                 'name', 'email', 'avatar_url', 'github_id', 'github_login', 'projects',
                 'creator_milestones', 'sender_milestones', 'creator_issues', 'sender_issues',
                 'assignee_issues', 'closedby_issues',
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


class OrganizationSerializer(serializers.ModelSerializer):
    '''
    Serialize the model Organization
    '''

    class Meta:
        model = Organization
        fields = (
                'github_id', 'name', 'description', 'html_url', 'avatar_url',
        )


class ProjectPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10000000

    class Meta:
        object_serializer_class = ProjectSerializer
