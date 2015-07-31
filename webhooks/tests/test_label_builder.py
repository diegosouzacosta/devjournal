# coding: utf-8
from datetime import datetime

from django.test import TestCase

from journal.models import Developer, Label, Project, Organization
from webhooks.builders import label_builder


class LabelBuilderTestCase(TestCase):
    def test_new_label(self):
        organization, __ = Organization.objects.get_or_create(
            github_id=1,
            defaults={
                'name': 'teste',
            }
        )

        developer, __ = Developer.objects.get_or_create(
            github_id=1,
            defaults={
                'github_login': 'test',
            }
        )

        project, __ = Project.objects.get_or_create(
            github_id=1,
            defaults={
                'name': 'test',
                'created_at': datetime.now(),
                'creator': developer,
                'organization': organization,
            }
        )

        count = Label.objects.count()

        created = label_builder({
            "name": "bug",
            "color": "f29513",
        }, project=project)

        assert Label.objects.count() == count + 1, 'a new label must be created'

        same = label_builder({
            "name": "bug",
            "color": "f29513",
        }, project=project)

        assert Label.objects.count() == count + 1, 'the same label must be returned'
        assert created == same, 'the same label must be returned'
