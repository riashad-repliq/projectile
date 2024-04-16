from django.urls import reverse
"""PUBLIC ME URLS"""

def me_shop_list_create_url():
    return reverse('shops')

def me_shop_details_url():
    return reverse('retrieve-shop')

"""PRIVATE WE URLS"""

def me_shop_list_create_url():
    return reverse('shops')

def we_update_delete_shop_url(shop_uuid:str):
    return reverse('manage-shop', args=[shop_uuid])