# coding: utf-8

import json

from django.test import TestCase

from journal.models import Milestone
from webhooks.builders import developer_builder, milestone_builder


class MilestoneBuilderTestCase(TestCase):
    def test_project_builder_new_project(self):
        count = Milestone.objects.count()
        with open('webhooks/tests/data/milestone.json') as json_file:
            milestone_json = json.load(json_file)

        milestone = milestone_builder(project_json, project)
        self.assertEqual(Milestone.objects.count(), count + 1)
        self.assertEqual(milestone.github_id, project_json.get('id'))
        self.assertEqual(milestone.number, project_json.get('number'))
        self.assertEqual(milestone.state, project_json.get('state'))
        self.assertEqual(milestone.title, project_json.get('title'))
        self.assertEqual(milestone.description, project_json.get('description'))
        self.assertEqual(milestone.html_url, project_json.get('html_url'))
        self.assertEqual(milestone.created_at, project_json.get('created_at'))
        self.assertEqual(milestone.closed_at, project_json.get('created_at'))
        self.assertEqual(milestone.updated_at, project_json.get('updated_at'))
        self.assertEqual(milestone.due_on, project_json.get('due_on'))
