import uuid
from django.db import models

class AbstractBaseModel(models.Model):
    uuid = models.UUIDField( default=uuid.uuid4(), unique=True, editable=False)





"""a helper method to find attributes associated with an extra SerializerMethodField"""
def get_attribute(instance, model, attribute):
    if hasattr(instance, model):
        return getattr(getattr(instance, model), attribute, None)