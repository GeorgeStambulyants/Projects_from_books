from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase

import base64
import json
from unittest.mock import patch

from . models import Subscriber, MailingList
from . factories import SubscriberFactory


class MockSendEmailToSubscriberTask:

    def setUp(self):
        self.send_confirmation_email_patch = patch(
            'mailinglist.tasks.send_confirmation_email_to_subscriber'
        )
        self.send_confirmation_email_mock = self.send_confirmation_email_patch.start()
        super().setUp()

    def tearDown(self):
        self.send_confirmation_email_patch.stop()
        self.send_confirmation_email_mock = None
        super().tearDown()


class SubscriberCreationTestCase(MockSendEmailToSubscriberTask, TestCase):

    def test_calling_create_queues_confirmation_email_task(self):
        user = get_user_model().objects.create_user(
            username='unit test runner'
        )
        mailing_list = MailingList.objects.create(
            name='unit test',
            owner=user,
        )
        Subscriber.objects.create(
            email='unittest@example.com',
            mailing_list=mailing_list
        )

        self.assertEqual(self.send_confirmation_email_mock.delay.call_count, 1)


class SubscriberManagerTestCase(TestCase):
    
    def test_confirmed_subscribed_for_mailingList(self):
        mailing_list = MailingList.objects.create(
            name='unit test',
            owner=get_user_model().objects.create_user(
                username='unit test'
            )
        )
        confirmed_users = [
            SubscriberFactory(mailing_list=mailing_list)
            for _ in range(3)
        ]
        confirmed_users_qs = Subscriber.objects.confirmed_subscribers_for_mailing_list(
            mailing_list=mailing_list
        )
        self.assertEqual(
            len(confirmed_users),
            confirmed_users_qs.count()
        )
        for user in confirmed_users_qs:
            self.assertIn(user, confirmed_users)


class ListMailingListsWithAPITestCase(APITestCase):

    def setUp(self):
        password = 'password'
        username = 'unit test'
        self.user = get_user_model().objects.create_user(
            username=username,
            password=password
        )
        cred_bytes = '{}:{}'.format(username, password).encode('utf-8')
        self.basic_auth = base64.b64encode(cred_bytes).decode('utf-8')
    
    def test_listing_all_my_mailing_lists(self):
        mailing_lists = [
            MailingList.objects.create(
                name='unit test {}'.format(i),
                owner=self.user
            )
            for i in range(3)
        ]

        self.client.credentials(
            HTTP_AUTHORIZATION=f'Basic {self.basic_auth}'
        )
        response = self.client.get(
            '/mailinglist/api/v1/mailing-list'
        )
        self.assertEqual(200, response.status_code)
        parsed = json.loads(response.content)
        self.assertEqual(3, len(parsed))

        content = str(response.content)
        for ml in mailing_lists:
            self.assertIn(str(ml.id), content)
            self.assertIn(ml.name, content)
