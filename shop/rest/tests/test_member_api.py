from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
import json

from common.tests.base_test import BaseTest
from shop.models import Shop, Member
from . import payloads, urlhelpers
from core.rest.tests.payloads import user_create_payload
User = get_user_model()

class MemberTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.client.force_authenticate(user=self.user)
        shop_creation = self.client.post(urlhelpers.me_shop_list_create_url(), payloads.shop_create_payload())
        self.shop =get_object_or_404(Shop, uuid=shop_creation.data['uuid'])

    def test_member_list(self):
        response = self.client.get(urlhelpers.member_list_create_url(self.shop.uuid))
        # print (json.dumps(response.data, indent=4))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_member_create(self):


        new_user= User.objects.create(
            phone_number = user_create_payload()['phone_number'],
            password= user_create_payload()['password'],
            username= user_create_payload()['username']
            )
        new_user_uuid = new_user.uuid

        payload = payloads.member_create_payload()
        payload['user_uuid'] = new_user_uuid
        payload['member_type'] = 'staff'

        response = self.client.post(urlhelpers.member_list_create_url(self.shop.uuid), payload)
        # print (json.dumps(response.data, indent=4))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
