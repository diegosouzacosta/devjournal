# -*- coding: utf8 -*-
# vim: ts=4 sts=4 sw=4 ent:

from django.db import models
from django.db.models import Count, F, Case, When


class DeveloperQuerySet(models.QuerySet):

    def get_extras_daily(self, date_start, date_end):
        '''Returns:
        Get values for Organization building by time
        '''
        return self.annotate(
            issues_closed=Count(
                Case(
                    When(
                        organization__projects__milestones__issues__closed_at__gte=date_start,
                        organization__projects__milestones__issues__closed_at__lte=date_end,
                        then=1,
                    )
                ),
            ),
            issues_open=Count(
                Case(
                    When(
                        organization__projects__milestones__issues__created_at__gte=date_start,
                        organization__projects__milestones__issues__created_at__lte=date_end,
                        then=1,
                    )
                ),
            ),
            issues_progress=Count(
                Case(
                    When(
                        organization__projects__milestones__issues__label__name__icontains='progress',
                        then=1,
                    )
                ),
            ),
            milestone_open=Count(
                Case(
                    When(
                        organization__projects__milestones__state__icontains='open',
                        then=1,
                    )
                ),
            ),
            milestone_percent=Count(
                Case(
                    When(
                        organization__projects__milestones__issues__state__icontains='close',
                        then=1,
                    )
                ),
            ) / Count(F('organization__projects__milestones__issues')),
        )


class DeveloperManager(models.Manager):

    def get_queryset(self):
        return DeveloperQuerySet(self.model, using=self._db)

    def get_values_daily(self, date_start, date_end, organization):
        return self.get_queryset().filter(
            organization__projects__milestones__issues__updated_at__gte=date_start,
            organization__projects__milestones__issues__updated_at__lte=date_end,
            organization__projects__milestones__issues__sender=F('pk'),
            organization=organization,
        ).get_extras_daily(date_start, date_end)


class ProjectQuerySet(models.QuerySet):

    def get_extras_daily(self, date_start, date_end):
        '''Returns:
        Get values for Organization building by time
        '''
        return self.annotate(
            issues_closed=Count(
                Case(
                    When(
                        milestones__issues__closed_at__gte=date_start,
                        milestones__issues__closed_at__lte=date_end,
                        then=1,
                    )
                ),
            ),
            issues_open=Count(
                Case(
                    When(
                        milestones__issues__created_at__gte=date_start,
                        milestones__issues__created_at__lte=date_end,
                        then=1,
                    )
                ),
            ),
            issues_progress=Count(
                Case(
                    When(
                        milestones__issues__label__name__icontains='progress',
                        then=1,
                    )
                ),
            ),
            milestone_open=Count(
                Case(
                    When(
                        milestones__state__icontains='open',
                        then=1,
                    )
                ),
            ),
            milestone_percent=Count(
                Case(
                    When(
                        milestones__issues__state__icontains='close',
                        then=1,
                    )
                ),
            ) / Count(F('milestones__issues')),
        )


class ProjectManager(models.Manager):

    def get_queryset(self):
        return ProjectQuerySet(self.model, using=self._db)

    def get_values_weekly(self, date_start, date_end, organization):
        return self.get_queryset().filter(
            milestones__issues__updated_at__gte=date_start,
            milestones__issues__updated_at__lte=date_end,
            milestones__issues__sender=F('pk'),
            organization=organization,
        ).get_extras_daily(date_start, date_end)
