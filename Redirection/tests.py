from django.test import TestCase
from .models import Redirect
from django.core.cache import cache

# Create your tests here.


class RedirectTestCase(TestCase):
    def setUp(self):
        Redirect.objects.create(
            key='primera', url="http://www.primeraweb.com", active=True)
        Redirect.objects.create(
            key='segunda', url="http://www.segundaweb.com", active=False)

    def test_if_cached(self):
        """
            Chequea que en la creación de instancias se cree la clave en el cache.
        """
        self.assertEqual(cache.get("primera"), "http://www.primeraweb.com")
        self.assertEqual(cache.get("segunda"), None)

    def test_when_update(self):
        """
            Chequea que funcione la signal de actualización.
        """
        primera = Redirect.objects.get(key="primera")
        segunda = Redirect.objects.get(key="segunda")
        primera.active = False
        primera.save()
        segunda.active = False
        segunda.save()
        self.assertEqual(cache.get("primera"), None)
        self.assertEqual(cache.get("segunda"), None)

        primera.active = True
        primera.url = "http://www.primeraactualizadaweb.com"
        primera.save()
        segunda.active = True
        segunda.url = "http://www.segundaactualizadaweb.com"
        segunda.save()

        self.assertEqual(cache.get("primera"),
                         "http://www.primeraactualizadaweb.com")
        self.assertEqual(cache.get("segunda"),
                         "http://www.segundaactualizadaweb.com")
