# coding: utf-8
from django.test import TestCase
from django.db.utils import IntegrityError

from journal.models import Developer
from webhooks.builders import developer_builder


class DeveloperBuilderTestCase(TestCase):
    def test_developer(self):
        count = Developer.objects.count()

        create_login = 'test-{}'.format(count + 1)
        create_name = 'test-name-{}'.format(count + 1)
        create_email = 'test-email-{}'.format(count + 1)

        created = developer_builder({
            'id': count + 1,
            'avatar_url': '',
            'github_login': create_login,
            'name': create_name,
            'email': create_email,
        })

        assert Developer.objects.count() == count + 1, 'a new developer must be created'

        same = developer_builder({
            'id': count + 1,
            'avatar_url': '',
            'github_login': create_login,
            'name': create_name,
            'email': create_email,
        })

        assert Developer.objects.count() == count + 1, 'the same developer must be returned'
        assert created == same, 'the same developer must be returned'

        with self.assertRaises(IntegrityError):
            developer_builder({
                'id': count + 2,
                'avatar_url': '',
                'github_login': create_login,  # same login
                'name': create_name,
                'email': create_email,
            })
