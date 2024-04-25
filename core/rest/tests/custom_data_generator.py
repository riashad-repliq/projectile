from faker.providers import BaseProvider

# from PIL import Image
# from io import BytesIO


class CustomDataGenerator(BaseProvider):
    def generate_phone_number(self):
        sim = str(self.random_element(["17", "18", "19", "16", "15"]))
        suffix = str(self.random_int(min=10000000, max=99999999))
        return "+880" + sim + suffix


# def generate_fake_image():
#     width, height = 300, 300
#     color = (255, 255, 255)
#     image = Image.new("RGB", (width, height), color)
#     fake_io = BytesIO()
#     image.save(fake_io, 'PNG')
#     fake_io.seek(0)
#     return fake_io


# import tempfile

# # Generate a fake image and save it to a temporary file with a specified extension
# def generate_fake_image_file(extension='jpg'):
#     fake_image = generate_fake_image()  # Assuming you have a generate_fake_image() function
#     temp_file = tempfile.NamedTemporaryFile(suffix='.' + extension, delete=False)
#     temp_file.write(fake_image.read())
#     temp_file.close()
#     return temp_file.name

# # Usage example with extension 'png'
# fake_image_file_path = generate_fake_image_file(extension='jpg')
