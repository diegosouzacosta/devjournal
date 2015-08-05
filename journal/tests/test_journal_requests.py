# -*- coding: utf8 -*-
# vim: ts=4 sts=4 sw=4 et:

from django.test import TestCase


class JournalRequestsTestCase(TestCase):

    fixtures = [
        'config.json',
        'label.json',
        'milestone.json',
        'project.json',
        'developer.json',
        'manager.json',
        'organization.json',
    ]

    def test_response_journal_daily(self):
        url = '/journal/daily/'
        response = self.client.get(url, {
            'organization': 1,
            'date-start': '2015-07-30',
            'date-end': '2015-08-01'
        })
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response['Content-Type'], 'application/json')

    def test_response_journal_weekly(self):
        url = '/journal/weekly/'
        response = self.client.get(url, {
            'organization': 1,
            'date-start': '2015-07-30',
            'date-end': '2015-08-01'
        })
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response['Content-Type'], 'application/json')

        url = '/journal/'
        response = self.client.get(url, {
            'organization': 1,
            'date-start': '2015-07-30',
            'date-end': '2015-08-01'
        })
        self.assertEquals(response.status_code, 404)
        self.assertEquals(response['Content-Type'], 'text/html')
