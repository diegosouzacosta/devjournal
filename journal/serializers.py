# -*- coding: utf-8 -*-
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

    label_name = serializers.ReadOnlyField(source='label.name')
    label_color = serializers.ReadOnlyField(source='label.color')

    class Meta:
        model = Issue
        fields = (
            'github_id', 'number', 'state', 'title', 'body', 'html_url', 'created_at', 'closed_at', 'updated_at',
            'due_on', 'project', 'milestone', 'label_name', 'label_color', 'creator', 'sender', 'assignee',
            'closed_by'
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


class MilestoneSerializer(serializers.ModelSerializer):
    '''
    Serialize the model Milestone
    '''

    issues = serializers.SerializerMethodField('get_issue')

    class Meta:
        model = Milestone
        fields = (
            'github_id', 'number', 'state', 'title', 'description', 'html_url', 'created_at',
            'closed_at', 'updated_at', 'due_on', 'project', 'creator', 'issues',
        )

    def get_issue(self, milestone):
        issues = milestone.issues.filter(sender=milestone.developer_id).distinct('github_id')
        serializer = IssueSerializer(instance=issues, many=True)
        return serializer.data


class ProjectSerializer(serializers.ModelSerializer):
    '''
    Serialize the model Projects
    '''

    milestones = serializers.SerializerMethodField('get_milestone')

    class Meta:
        model = Project
        fields = (
            'id', 'github_id', 'name', 'description', 'html_url', 'created_at', 'milestones',
        )

    def get_milestone(self, project):
        milestones = Milestone.objects.filter(
            issues__sender=project.developer_id).distinct('github_id').extra(
            select={'developer_id': project.developer_id}
        )
        serializer = MilestoneSerializer(instance=milestones, many=True)
        return serializer.data


class ProjectWeeklySerializer(serializers.ModelSerializer):
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

    def get_project(self, organization):
        organizations = organization.projects.distinct('github_id')
        serializer = ProjectSerializer(instance=organizations, many=True)
        return serializer.data



class DeveloperSerializer(serializers.ModelSerializer):
    '''
    Serialize the model Developer
    '''

    configs = ConfigSerializer(many=True, read_only=True)
    issues_closed = serializers.IntegerField(read_only=True)
    issues_open = serializers.IntegerField(read_only=True)
    issues_progress = serializers.IntegerField(read_only=True)
    milestone_open = serializers.IntegerField(read_only=True)
    milestone_percent = serializers.IntegerField(read_only=True)
    projects = serializers.SerializerMethodField('get_project')

    class Meta:
        model = Developer
        fields = (
            'configs', 'avatar_url', 'github_login', 'github_id', 'issues_closed', 'issues_open', 'issues_progress',
            'milestone_open', 'milestone_percent', 'projects',
        )

    def get_milestone(self, developer):
        milestones = Milestone.objects.filter(issues__sender=developer.pk)
        return milestones

    def get_project(self, developer):
        projects = Project.objects.filter(
            milestones__in=self.get_milestone(developer)).extra(
            select={'developer_id': developer.pk}).distinct('github_id')
        serializer = ProjectSerializer(instance=projects, many=True)
        return serializer.data


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
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 10000000

    class Meta:
        object_serializer_class = DeveloperSerializer


class ProjectWeeklyPagination(PageNumberPagination):
    page_size =30
    page_size_query_param = 'page_size'
    max_page_size = 10000000

    class Meta:
        object_serializer_class = ProjectWeeklySerializer
