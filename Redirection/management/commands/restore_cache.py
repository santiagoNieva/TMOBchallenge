from django.core.management import BaseCommand
from Redirection.models import Redirect
from django.core.cache import cache

class Command(BaseCommand):
    help = "Comando utilizado para restaurar el cache en caso de que se haya perdido por cualquiera motivo."

    def handle(self,*args, **options):
        self.stdout.write(self.style.SUCCESS(self.help))

        self.stdout.write(self.style.SUCCESS("Se recorren todas las instancias. La demora varía por el tamaño de la tabla."))
        
        for instance in Redirect.objects.all():
            if instance.active:
                cache.set(instance.key,instance.url)
            else:
                cache.delete(instance.key)
                
        self.stdout.write(self.style.SUCCESS("Cache Actualizada."))