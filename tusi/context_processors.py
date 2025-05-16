from .models import Footer
from oferta_podstrony.models import Oferta_pozycja

def oferta_pozycje_context(request):
    return {
        'oferta_pozycje': Oferta_pozycja.objects.all()
    }


def stopka_context(request):
    return {
        'footer': Footer.objects.first()
    }
