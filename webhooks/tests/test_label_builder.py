# coding: utf-8

from django.test import TestCase

from journal.models import Label
from webhooks.builders import label_builder


class LabelParserTestCase(TestCase):
    def test_new_label(self):
        count = Label.objects.count()

        label_builder({
            "name": "bug",
            "color": "f29513",
        })

        assert Label.objects.count() == count + 1
