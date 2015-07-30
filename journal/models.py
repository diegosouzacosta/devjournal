# -*- coding: utf8 -*-
# vim: ts=4 sts=4 sw=4 et:

from django.db import models


class Organization(models.Model):

    github_id = models.IntegerField(verbose_name=u'ID GitHub', unique=True)
    name = models.TextField()
    description = models.TextField(null=True, blank=True)
    html_url = models.TextField(null=True, blank=True)
    avatar_url = models.TextField(null=True, blank=True)


class Projects(models.Model):

    github_id = models.IntegerField(verbose_name=u'ID GitHub', unique=True)
    name = models.TextField()
    description = models.TextField(null=True, blank=True)
    html_url = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField()
