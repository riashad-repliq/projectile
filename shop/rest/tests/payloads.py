from faker import Faker

fake = Faker()

def shop_create_payload():
    return{
        'name': fake.name(),
        'location': fake.name(),
    }

def member_create_payload():
    return{
        'user_uuid': None,
        'member_type': ''
    }

