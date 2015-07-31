# -*- coding: utf8 -*-
# vim: ts=4 sts=4 sw=4 ent:

from django.db import models
from django.db.models import Avg, Min, Max, Count, F, Sum, Case, When


class DeveloperQuerySet(models.QuerySet):

    def get_queries_summaries(self):
        '''Returns:
        Get values for Organization building by time
        '''
        return self.annotate(

        )


class DeveloperManager(models.Manager):

    def get_queryset(self):
        return DeveloperQuerySet(self.model, using=self._db)

    def get_values(self, date_start, date_end, organization):
        return self.get_queryset().filter(
            organization__projects__milestones__issues__update_at__range=[date_start, date_end],
            organization=organization,
        )
