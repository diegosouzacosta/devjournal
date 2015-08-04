# coding: utf-8

import json

from django.test import TestCase

from journal.models import Issue
from webhooks.builders import issue_builder


class IssueBuilderTestCase(TestCase):
    def test_issue_builder_new_issue(self):
        count = Issue.objects.count()

        with open('webhooks/tests/data/issue.json', 'r') as issue_json:
            issue_json = json.load(issue_json)

        issue = issue_builder(issue_json)
        self.assertEqual(Issue.objects.count(), count + 1)
        self.assertEqual(issue.github_id, issue_json['issue']['id'])
        self.assertEqual(issue.number, issue_json['issue']['number'])
        self.assertEqual(issue.action, issue_json['action'])
        self.assertEqual(issue.state, issue_json['issue']['state'])
        self.assertEqual(issue.title, issue_json['issue']['title'])
        self.assertEqual(issue.body, issue_json['issue']['body'])
        self.assertEqual(issue.html_url, issue_json['issue']['html_url'])
        self.assertEqual(issue.created_at, issue_json['issue']['created_at'])
        self.assertEqual(issue.closed_at, issue_json['issue']['closed_at'])
        self.assertEqual(issue.updated_at, issue_json['issue']['updated_at'])
        self.assertEqual(issue.assignee, issue_json['issue']['assignee'])
