# coding: utf-8

from journal.models import Developer, Organization, Label, Project


ISSUE = 'issue'


def builder(github_event, json_object):
    if github_event == ISSUE:
        issue_builder(json_object)


def issue_builder(json_object):
    pass


def label_builder(json_object, project):
    name = json_object['name']
    color = json_object['color']

    label, __ = Label.objects.get_or_create(
        name=name,
        project=project,
        defaults={'color': color},
    )

    return label_create_if_changed(label, json_object, project)


def label_create_if_changed(label, json_object, project):
    if label.color != json_object['color']:
        return Label.objects.create(
            name=json_object['name'],
            project=project,
            color=json_object['color'],
        )

    return label


def organization_builder(json_object):
    github_id = json_object.get('id')
    organization = Organization.objects.filter(github_id=github_id).first()

    if organization:
        organization.github_id = json_object.get('id')
        organization.name = json_object.get('login')
        organization.description = json_object.get('description')
        organization.html_url = json_object.get('url')
        organization.avatar_url = json_object.get('avatar_url')
        organization.save()
        return organization

    return Organization.objects.create(
        github_id=json_object.get('id'),
        name=json_object.get('login'),
        description=json_object.get('description'),
        html_url=json_object.get('url'),
        avatar_url=json_object.get('avatar_url')
    )


def project_builder(json_object):
    github_id = json_object.get('id')
    project = Project.objects.filter(github_id=github_id).first()

    if project:
        project.github_id = json_object.get('id')
        project.name = json_object.get('name')
        project.description = json_object.get('description')
        project.html_url = json_object.get('url')
        project.created_at = json_object.get('created_at')
        project.creator = developer_builder(json_object.get('owner'))
        project.save()
        return project

    return Project.objects.create(
        github_id=json_object.get('id'),
        name=json_object.get('name'),
        description=json_object.get('description'),
        html_url=json_object.get('url'),
        created_at=json_object.get('created_at'),
        creator=developer_builder(json_object.get('owner'))
    )


def developer_builder(json_object):
    developer, __ = Developer.objects.get_or_create(
        github_id=json_object['id'],
        defaults={
            'avatar_url': json_object['avatar_url'],
            'github_login': json_object['github_login'],
        }
    )

    if developer.avatar_url != json_object['avatar_url']:
        developer.avatar_url = json_object['avatar_url']
        developer.save()
