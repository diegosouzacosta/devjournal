# coding: utf-8

from journal.models import Organization, Label


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
    pass


def organization_builder(json_object):
    github_id = json_object.get('id')
    organization = Organization.objects.filter(github_id=github_id).first()

    if organization:
        organization.github_id=json_object.get('id')
        organization.name=json_object.get('login')
        organization.description=json_object.get('description')
        organization.html_url=json_object.get('url')
        organization.avatar_url=json_object.get('avatar_url')
        organization.save()
        return organization

    return Organization.objects.create(
        github_id=json_object.get('id'),
        name=json_object.get('login'),
        description=json_object.get('description'),
        html_url=json_object.get('url'),
        avatar_url=json_object.get('avatar_url')
    )
