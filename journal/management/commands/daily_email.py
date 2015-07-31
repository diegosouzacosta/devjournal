# -*- coding: utf-8 -*-
import simplejson as json
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.template import Context
from django.template.loader import get_template

import requests

from journal.models import Organization


class Command(BaseCommand):
    help = 'Send daily email by users'
    can_import_settings = True

    def add_arguments(self, parser):
        parser.add_argument('organization')

    def handle(self, *args, **options):
        try:
            organization = Organization.objects.get(name=options['organization'])
        except Organization.DoesNotExist:
            raise CommandError('Organization not found: {}'.format(options['organization']))

        daily_api = settings.API_SERVER + reverse('journal:daily')
        today = datetime.now()
        yesterday = today - timedelta(1)

        params = {
            'organization': organization.pk,
            'date-start': yesterday.strftime('%Y-%m-%d'),
            'date-end': today.strftime('%Y-%m-%d'),
        }
        response = requests.get(daily_api, params=params)

        if response.status_code != 200:
            log_message = 'API response returned status code different than 200: Status Code {}'
            raise CommandError(log_message.format(response.status_code))

        try:
            content = json.loads(response.content)
        except json.JSONDecodeError:
            raise CommandError('Error to load the response json')

        template = get_template('journal/email/daily.html')

        send_mail(
            'DevJornal - {}'.format(organization.name),
            '',
            settings.EMAIL_HOST_USER,
            # [manager.email for manager in organization.journal_manager.all()],
            ['dudu@axado.com.br'],
            html_message=template.render(Context(content))
        )
