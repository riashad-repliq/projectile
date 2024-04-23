from faker import Faker
import requests

faker = Faker()
# fake_image_url = faker.image_url()
# response = requests.get(fake_image_url)
# with open('fake_image.jpg', 'wb') as f:
#     f.write(response.content)


def product_create_payload():
    return{
        'shop': None,
        'name': faker.name(),
        'description': faker.sentence(),
        'product_profile_image': '',
        'price': faker.random_int(min=10, max=100),
        'quantity': faker.random_int(min=100, max=600),

    }

def product_update_payload():
    price = faker.random_int(min=1, max=222)
    formatted_price = "{:.2f}".format(price)
    return{
        'description': faker.sentence(),
        'price': formatted_price,
        'quantity': {
            'quantity': faker.random_int(min=100, max=600)
        }
    }
