# -*- coding: utf8 -*-
# vim: ts=4 sts=4 sw=4 et:

from django.contrib import admin
from journal.models import Organization, Manager, Developer, Project, Milestone, Label, Issue, Config


admin.site.register(Organization)
admin.site.register(Manager)
admin.site.register(Developer)
admin.site.register(Project)
admin.site.register(Milestone)
admin.site.register(Label)
admin.site.register(Issue)
admin.site.register(Config)
