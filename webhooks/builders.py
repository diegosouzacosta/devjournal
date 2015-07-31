# coding: utf-8

from devjournal.models import Label


ISSUE = 'issue'


def builder(github_event, json_object):
    if github_event == ISSUE:
        issue_builder(json_object)


def issue_builder(json_object):
    pass


def label_builder(json_object):
    name = json_object['name']
    color = json_object['color']

    label = Label.objects.get_or_create(
        name=name,
        defaults={'color': color},
    )

    return label_create_if_changed(label, json_object)


def label_create_if_changed(label, json_object):
    if label.color != json_object['color']:
        return Label.objects.create(
            name=json_object['name'],
            color=json_object['color'],
        )

    return label


def label_create_if_not_exists(json_object):
