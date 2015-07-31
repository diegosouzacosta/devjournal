# -*- coding: utf8 -*-
# vim: ts=4 sts=4 sw=4 et:

from django.db import models

from journal.managers import DeveloperManager


class Organization(models.Model):

    github_id = models.IntegerField(verbose_name=u'ID GitHub', unique=True)
    name = models.TextField()
    description = models.TextField(null=True, blank=True)
    html_url = models.TextField(null=True, blank=True)
    avatar_url = models.TextField(null=True, blank=True)


class JournalUser(models.Model):

    name = models.CharField(unique=True, max_length=150)
    email = models.EmailField(unique=True)
    organization = models.ForeignKey(Organization, related_name=u'%(app_label)s_%(class)s')

    class Meta:
        abstract = True


class Manager(JournalUser):
    pass


class Developer(JournalUser):

    avatar_url = models.CharField(verbose_name=u'Avatar Url', unique=True, max_length=200, null=True, blank=True)
    github_id = models.IntegerField(verbose_name=u'ID GitHub', unique=True)
    github_login = models.CharField(verbose_name=u'Login GitHub', unique=True, max_length=100)
    objects = DeveloperManager()


class Project(models.Model):

    github_id = models.IntegerField(verbose_name=u'ID GitHub', unique=True)
    name = models.TextField()
    description = models.TextField(null=True, blank=True)
    html_url = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField()
    creator = models.ForeignKey(Developer, related_name=u'projects')
    organization = models.ForeignKey(Organization, related_name=u'projects')


class Milestone(models.Model):

    github_id = models.IntegerField(verbose_name=u'ID GitHub', unique=True)
    number = models.IntegerField(unique=True)
    state = models.CharField(max_length=15)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    html_url = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField()
    close_at = models.DateTimeField(null=True, blank=True)
    update_at = models.DateTimeField()
    due_on = models.DateTimeField(null=True, blank=True)
    project = models.ForeignKey(Project, db_column='project_id', related_name=u'milestones')
    creator = models.ForeignKey(Developer, related_name=u'creator_milestones')
    sender = models.ForeignKey(Developer, null=True, blank=True, related_name=u'sender_miletones')


class Label(models.Model):

    name = models.TextField()
    color = models.CharField(max_length=10, null=True, blank=True)


class Issue(models.Model):

    github_id = models.IntegerField(verbose_name=u'ID GitHub', unique=True)
    number = models.IntegerField(unique=True)
    state = models.CharField(max_length=15)
    title = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    html_url = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField()
    close_at = models.DateTimeField(null=True, blank=True)
    update_at = models.DateTimeField()
    due_on = models.DateTimeField(null=True, blank=True)
    project = models.ForeignKey(Project, db_column='project_id', related_name=u'issues')
    milestone = models.ForeignKey(Milestone, db_column='milestone_id', related_name=u'issues')
    labels = models.ForeignKey(Label, db_column='label_id', related_name=u'issues')
    creator = models.ForeignKey(Developer, related_name=u'creator_issues')
    sender = models.ForeignKey(Developer, null=True, blank=True, related_name='sender_issues')
    assignee = models.ForeignKey(Developer, null=True, blank=True, related_name=u'assignee_issues')
    closed_by = models.ForeignKey(Developer, null=True, blank=True, related_name=u'closedby_issues')


class Config(models.Model):

    projects = models.ManyToManyField(Project, db_column=u'config_manager', related_name=u'configs')
    manager = models.ForeignKey(Manager)
    weekly = models.BooleanField(default=True)
    daily = models.BooleanField(default=True)
