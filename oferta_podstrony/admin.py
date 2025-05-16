from django.contrib import admin
from django import forms
from .models import Oferta_pozycja, Post
from tusi.admin import BasePageAdmin


# usuwanie slug z widoczności
class Oferta_pozycjaForm(forms.ModelForm):

    class Meta:
        model = Oferta_pozycja
        exclude = ('slug',)

class Oferta_pozycjaAdmin(BasePageAdmin):
    form = Oferta_pozycjaForm



class PostAdmin(BasePageAdmin):
    list_display = ['oferta_pozycja', 'nazwa', 'styl', 'kolor', 'kolejnosc']  # Wyświetlane kolumny
    search_fields = ('nazwa',)  # Możliwość wyszukiwania po nazwie
    list_editable = ['oferta_pozycja', 'styl', 'kolor', 'kolejnosc']  # Edytowalne pole: oferta_pozycja
    list_display_links = ('nazwa',)  # Tylko 'nazwa' będzie linkiem do edycji
    ordering = ['kolejnosc']
    list_filter = ['oferta_pozycja']


admin.site.register(Post, PostAdmin)
admin.site.register(Oferta_pozycja, Oferta_pozycjaAdmin)