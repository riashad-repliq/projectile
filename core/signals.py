from django.db.models import Avg
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from product.models import CustomerReview

User= get_user_model()


@receiver(post_delete, sender=User)

def update_product_average_rating(sender, instance, **kwargs):
    reviews = CustomerReview.objects.filter(user=instance)
    for review in reviews:
        product = review.product
        ratings = CustomerReview.objects.filter(product=product)
        if ratings.exists():
            product.average_rating = ratings.aggregate(Avg("rating"))["rating__avg"]
        else:
            product.average_rating = None
        product.save()
