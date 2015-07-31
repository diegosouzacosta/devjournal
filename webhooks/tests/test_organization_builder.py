# coding: utf-8

from django.test import TestCase

from journal.models import Organization
from webhooks.builders import organization_builder


class OrganizationBuilderTestCase(TestCase):
    def test_organization_builder_new_organization(self):
        count = Organization.objects.count()

        organization_json = {
            "login": "github",
            "id": 2,
            "url": "https://api.github.com/orgs/github",
            "avatar_url": "https://github.com/images/error/octocat_happy.gif",
            "description": "A great organization"
        }

        organization = organization_builder(organization_json)
        self.assertEqual(Organization.objects.count(), count + 1)
        self.assertEqual(organization.github_id, organization_json.get('id'))
        self.assertEqual(organization.name, organization_json.get('login'))
        self.assertEqual(organization.description, organization_json.get('description'))
        self.assertEqual(organization.html_url, organization_json.get('url'))
        self.assertEqual(organization.avatar_url, organization_json.get('avatar_url'))

    def test_organization_builder_old_organization(self):
        count = Organization.objects.count()

        organization_json = {
            "login": "github",
            "id": 3,
            "url": "https://api.github.com/orgs/github",
            "avatar_url": "https://github.com/images/error/octocat_happy.gif",
            "description": "A great organization"
        }

        organization = organization_builder(organization_json)
        self.assertEqual(Organization.objects.count(), count + 1)
        count = Organization.objects.count()

        organization = organization_builder(organization_json)
        self.assertEqual(Organization.objects.count(), count)
        self.assertEqual(organization.github_id, organization_json.get('id'))
        self.assertEqual(organization.name, organization_json.get('login'))
        self.assertEqual(organization.description, organization_json.get('description'))
        self.assertEqual(organization.html_url, organization_json.get('url'))
        self.assertEqual(organization.avatar_url, organization_json.get('avatar_url'))

    def test_organization_builder_update_organization(self):
        count = Organization.objects.count()

        organization_json = {
            "login": "github",
            "id": 4,
            "url": "https://api.github.com/orgs/github",
            "avatar_url": "https://github.com/images/error/octocat_happy.gif",
            "description": "A great organization"
        }

        organization = organization_builder(organization_json)
        self.assertEqual(Organization.objects.count(), count + 1)
        count = Organization.objects.count()
        organization_json = {
            "login": "github2",
            "id": 1,
            "url": "https://api.github.com/orgs/github2",
            "avatar_url": "https://github.com/images/error/octocat_happy2.gif",
            "description": "A great organization2"
        }

        organization = organization_builder(organization_json)
        self.assertEqual(Organization.objects.count(), count)
        self.assertEqual(organization.github_id, organization_json.get('id'))
        self.assertEqual(organization.name, organization_json.get('login'))
        self.assertEqual(organization.description, organization_json.get('description'))
        self.assertEqual(organization.html_url, organization_json.get('url'))
        self.assertEqual(organization.avatar_url, organization_json.get('avatar_url'))
