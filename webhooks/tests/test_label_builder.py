from django.test import TestCase

from devjournal.models import Label
from webhooks import label_builder


class LabelParserTestCase(TestCase):
    def test_new_label(self):
        count = Label.objects.count()

        label_builder({
            "name": "bug",
            "color": "f29513",
        })

        assert Label.objects.count() == count + 1
