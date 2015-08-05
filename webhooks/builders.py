# coding: utf-8

from journal.models import Developer, Organization, Label, Project, Milestone, Issue


ISSUE = ['issues']


def builder(github_event, json_object):
    if github_event in ISSUE:
        return issue_builder(json_object)


def issue_builder(json_object):
    sender = developer_builder(json_object['sender'])
    action = json_object['action']
    project = project_builder(json_object['repository'])
    json_object = json_object['issue']
    assignee = developer_builder(json_object['assignee'])
    milestone = milestone_builder(json_object['milestone'], project, sender)

    return Issue.objects.create(
        github_id=json_object['id'],
        number=json_object['number'],
        action=action,
        html_url=json_object['html_url'],
        closed_at=json_object['closed_at'],
        created_at=json_object['created_at'],
        updated_at=json_object['updated_at'],
        title=json_object['title'],
        body=json_object['body'],
        state=json_object['state'],
        creator=developer_builder(json_object['user']),
        assignee=assignee,
        milestone=milestone,
        project=project,
    )


def label_builder(json_object, project):
    if not json_object:
        return

    name = json_object['name']
    color = json_object['color']

    label = Label.objects.filter(name=name, project=project).last()

    if not label:
        return Label.objects.create(
            name=name,
            color=color,
            project=project,
        )

    if label.color != color:
        label.color = json_object['color']
        label.save()

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


def project_builder(json_object, organization=None):
    github_id = json_object.get('id')
    project = Project.objects.filter(github_id=github_id).first()

    if not project:
        project = Project.objects.create(
            github_id=json_object.get('id'),
            name=json_object.get('name'),
            description=json_object.get('description'),
            html_url=json_object.get('url'),
            created_at=json_object.get('created_at'),
            creator=developer_builder(json_object.get('owner')),
            organization=organization,
        )
        return project

    project.github_id = json_object.get('id')
    project.name = json_object.get('name')
    project.description = json_object.get('description')
    project.html_url = json_object.get('url')
    project.created_at = json_object.get('created_at')
    project.creator = developer_builder(json_object.get('owner'))
    project.organization = organization
    project.save()

    return project


def developer_builder(json_object):
    if not json_object:
        return None
    github_id = json_object['id']
    avatar_url = json_object['avatar_url']
    github_login = json_object['login']

    developer = Developer.objects.filter(github_id=github_id).last()

    if not developer:
        return Developer.objects.create(
            github_id=github_id,
            avatar_url=avatar_url,
            github_login=github_login,

        )

    developer.avatar_url = avatar_url
    developer.github_login = github_login
    developer.save()

    return developer


def milestone_builder(json_object, project, developer):
    if not json_object:
        return

    creator = developer_builder(json_object['creator'])
    milestone = Milestone.objects.filter(github_id=json_object['id'],).last()

    if milestone:
        milestone.github_id = json_object.get('id')
        milestone.number = json_object.get('number')
        milestone.state = json_object.get('state')
        milestone.title = json_object.get('title')
        milestone.description = json_object.get('description')
        milestone.html_url = json_object.get('html_url')
        milestone.created_at = json_object.get('created_at')
        milestone.closed_at = json_object.get('closed_at')
        milestone.updated_at = json_object.get('updated_at')
        milestone.due_on = json_object.get('due_on')
        milestone.project = project
        milestone.creator = developer

    return Milestone.objects.create(
        github_id=json_object['id'],
        number=json_object['number'],
        state=json_object['state'],
        title=json_object['title'],
        description=json_object['description'],
        html_url=json_object['html_url'],
        created_at=json_object['created_at'],
        closed_at=json_object['closed_at'],
        due_on=json_object['due_on'],
        updated_at=json_object['updated_at'],
        project=project,
        creator=creator,
    )
