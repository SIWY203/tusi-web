from django.contrib import admin
from django import forms
from .models import Aktualnosci, O_nas, Oferta, Galeria, Kontakt, Cennik, Footer, Home, Page
from oferta_podstrony.models import Oferta_pozycja
from .widgets import LinkSelectWidget


# BAZA -------------------------------------
class BasePageAdmin(admin.ModelAdmin):
    # widget z listą slugów dla danego pola
    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == "link_przycisku":
            field.widget = LinkSelectWidget()
        if db_field.name == "slug":
            field.label = "Adres"
        return field
    # anty-clear pola link_przycisku
    def save_model(self, request, obj, form, change):
        if change:
            original = obj.__class__.objects.get(pk=obj.pk)
            if not form.cleaned_data.get('link_przycisku'):
                obj.link_przycisku = original.link_przycisku
        super().save_model(request, obj, form, change)


# OFERTA_POZYCJA ----------------------------
class Oferta_pozycjaForm(forms.ModelForm):
    class Meta:
        model = Oferta_pozycja
        fields = '__all__'

class Oferta_pozycjaAdmin(BasePageAdmin):
    form = Oferta_pozycjaForm
    list_display = ('nazwa', 'slug', 'styl', 'kolejnosc')
    prepopulated_fields = {'slug': ('nazwa',)}
    list_editable = ['styl', 'kolor', 'kolejnosc']
    ordering = ('kolejnosc',)
 


# INNE ADMINY -----------------------------
class HomeAdmin(BasePageAdmin):
    list_display = ['nazwa', 'styl', 'kolor', 'kolejnosc']
    list_editable = ['styl', 'kolor', 'kolejnosc']
    ordering = ['kolejnosc']

class AktualnosciAdmin(BasePageAdmin):
    list_display = ['nazwa', 'styl', 'kolor', 'kolejnosc']
    list_editable = ['styl', 'kolor', 'kolejnosc']
    ordering = ['kolejnosc']
    
class O_nasAdmin(BasePageAdmin):
    list_display = ['nazwa', 'styl', 'kolor', 'kolejnosc']
    list_editable = ['styl', 'kolor', 'kolejnosc']
    ordering = ['kolejnosc']

class OfertaAdmin(BasePageAdmin):
    list_display = ['nazwa', 'styl', 'kolor', 'kolejnosc']
    list_editable = ['styl', 'kolor', 'kolejnosc']
    ordering = ['kolejnosc']

class GaleriaAdmin(BasePageAdmin):
    list_display = ['nazwa', 'styl', 'kolor', 'kolejnosc']
    list_editable = ['styl', 'kolor', 'kolejnosc']
    ordering = ['kolejnosc']

class KontaktAdmin(BasePageAdmin):
    list_display = ['nazwa', 'styl', 'kolor', 'kolejnosc']
    list_editable = ['styl', 'kolor', 'kolejnosc']
    ordering = ['kolejnosc']

class CennikAdmin(BasePageAdmin):
    list_display = ['nazwa', 'styl', 'kolor', 'kolejnosc']
    list_editable = ['styl', 'kolor', 'kolejnosc']
    ordering = ['kolejnosc']


# REJESTRACJA ------------------------------
admin.site.register(Home, HomeAdmin)
admin.site.register(Aktualnosci, AktualnosciAdmin)
admin.site.register(O_nas, O_nasAdmin)
admin.site.register(Oferta, OfertaAdmin)
admin.site.register(Galeria, GaleriaAdmin)
admin.site.register(Kontakt, KontaktAdmin)
admin.site.register(Cennik, CennikAdmin)
admin.site.register(Footer)

