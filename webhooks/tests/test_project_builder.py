# coding: utf-8

import json

from django.test import TestCase

from journal.models import Project
from webhooks.builders import project_builder, organization_builder


class ProjectBuilderTestCase(TestCase):
    def test_project_builder_new_project(self):
        organization = organization_builder({
            "login": "github",
            "id": 1,
            "url": "https://api.github.com/orgs/github",
            "avatar_url": "https://github.com/images/error/octocat_happy.gif",
            "description": "A great organization"
        })

        count = Project.objects.count()

        with open('webhooks/tests/data/project.json') as json_file:
            project_json = json.load(json_file)

        project = project_builder(project_json, organization)
        self.assertEqual(Project.objects.count(), count + 1)
        self.assertEqual(project.github_id, project_json.get('id'))
        self.assertEqual(project.name, project_json.get('name'))
        self.assertEqual(project.description, project_json.get('description'))
        self.assertEqual(project.html_url, project_json.get('url'))
        self.assertEqual(project.created_at, project_json.get('created_at'))
