# -*- coding: utf8 -*-
# vim: ts=4 sts=4 sw=4 et:

from django.contrib import admin
from journal.models import Organization, Manager, Developer, Project, Milestone, Label, Issue, Config


class ConfigAdmin(admin.ModelAdmin):
    fields = ('manager', 'projects', 'weekly', 'daily',)
    list_display = ('manager', 'weekly', 'daily',)
    list_filter = ('manager',)


class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('name', 'github_id', 'github_login', 'email',)
    list_filter = ('name',)
    search_fields = ('name', 'github_login',)


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'github_id', 'html_url',)
    list_filter = ('name',)
    search_fields = ('name',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'github_id', 'html_url', 'organization', 'creator',)
    list_filter = ('name', 'organization',)
    search_fields = ('name',)


class LabelAdmin(admin.ModelAdmin):
    list_display = ('name', 'project',)
    list_filter = ('project',)
    search_fields = ('name',)


class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('title', 'github_id', 'number', 'state', 'project', 'creator', 'created_at', 'closed_at',)
    list_filter = ('state', 'project', 'creator',)
    search_fields = ('title', 'project',)


class IssueAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'github_id', 'number', 'state', 'project', 'creator', 'sender', 'label', 'created_at', 'updated_at',
        'assignee', 'closed_by',
    )
    list_filter = ('state', 'project', 'creator', 'sender', 'label', 'closed_by', 'assignee',)
    search_fields = ('title', 'project',)


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Manager)
admin.site.register(Developer, DeveloperAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Milestone, MilestoneAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Config, ConfigAdmin)
