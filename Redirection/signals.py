from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
from .models import Redirect


@receiver(post_save, sender=Redirect)
def cache_redirect(instance, created, **kwargs):
    if instance.active:
        cache.set(instance.key, instance.url)
    else:
        cache.delete(instance.key)
