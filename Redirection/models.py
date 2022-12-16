from django.db import models
from django.core.cache import cache
import logging
logger = logging.getLogger('custom')

# Create your models here.


class Redirect(models.Model):
    key = models.CharField(max_length=255, unique=True)
    url = models.URLField(max_length=255)
    active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.key} : {self.url}"

    @classmethod
    def get_redirect(cls, key):
        # Obtengo la key del cache
        url = cache.get(key, None)
        # Si obtengo un valor lo devuelvo
        if url:
            return url
        # Si no obtengo nada, busco recién en la DB. Podría existir un error en el caché.
        else:
            # Debo intentar obtener el valor, y si no existe en la db, devuelvo None
            try:
                instance = cls.objects.filter(active=True).get(key=key)
            except Exception as e:
                logger.info(f"No existe la key '{key}'.")
                return None
            else:
                # Si llega a esto, significa que la instancia se encuentra activa, pero su valor no esta guardada en la caché. Hay que corregir.
                logger.warning(
                    f"La instancia con pk [{instance.pk}] con key: '{key}' se encontró activa pero no en el caché.")
                cache.set(instance.key, instance.url)
                return instance.url
