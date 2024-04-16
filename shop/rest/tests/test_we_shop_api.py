from django.shortcuts import get_object_or_404

from django.contrib.auth import get_user_model
from rest_framework import status

from common.tests.base_test import BaseTest

from shop.models import Shop

from . import payloads, urlhelpers
from core.rest.tests.payloads import user_create_payload


User = get_user_model()

class WeShopTest(BaseTest):
    def setUp(self):
        super().setUp()

        self.client.force_authenticate(user=self.user)
        shop_creation = self.client.post(urlhelpers.me_shop_list_create_url(), payloads.shop_create_payload())
        self.shop =get_object_or_404(Shop, uuid=shop_creation.data['uuid'])

    def test_get_shop_details(self):

        uuid = self.shop.uuid

        response = self.client.get(urlhelpers.we_update_delete_shop_url(shop_uuid=uuid))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_restrict_non_members_access(self):
        user_payload = user_create_payload()

        non_member = User.objects.create(
            phone_number=user_payload['phone_number'],
            password=user_payload['password'],
            username=user_payload['username'])

        self.client.force_authenticate(user=non_member)

        response = self.client.get(urlhelpers.we_update_delete_shop_url(shop_uuid=self.shop.uuid))

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
