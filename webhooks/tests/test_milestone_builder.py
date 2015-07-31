# coding: utf-8

import json

from django.test import TestCase

from journal.models import Milestone
from webhooks.builders import (
    developer_builder,
    milestone_builder,
    organization_builder,
    project_builder,
)


class MilestoneBuilderTestCase(TestCase):
    def test_project_builder_new_project(self):
        developer = developer_builder({
            'id': 1,
            'avatar_url': '',
            'login': 'teste',
            'name': 'teste',
            'email': 'teste',
        })

        organization = organization_builder({
            "login": "github",
            "id": 1,
            "url": "https://api.github.com/orgs/github",
            "avatar_url": "https://github.com/images/error/octocat_happy.gif",
            "description": "A great organization"
        })
        count = Milestone.objects.count()
        with open('webhooks/tests/data/project.json') as json_file:
            project_json = json.load(json_file)

        project = project_builder(project_json, organization)
        with open('webhooks/tests/data/milestone.json') as json_file:
            milestone_json = json.load(json_file)

        project = project_builder(project_json, organization)
        milestone = milestone_builder(milestone_json, project, developer)
        self.assertEqual(Milestone.objects.count(), count + 1)
        self.assertEqual(milestone.github_id, milestone_json.get('id'))
        self.assertEqual(milestone.number, milestone_json.get('number'))
        self.assertEqual(milestone.state, milestone_json.get('state'))
        self.assertEqual(milestone.title, milestone_json.get('title'))
        self.assertEqual(milestone.description, milestone_json.get('description'))
        self.assertEqual(milestone.html_url, milestone_json.get('html_url'))
        self.assertEqual(milestone.created_at, milestone_json.get('created_at'))
        self.assertEqual(milestone.closed_at, milestone_json.get('closed_at'))
        self.assertEqual(milestone.updated_at, milestone_json.get('updated_at'))
        self.assertEqual(milestone.due_on, milestone_json.get('due_on'))
