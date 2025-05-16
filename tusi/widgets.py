from django import forms
from django.urls import reverse
from oferta_podstrony.models import Oferta_pozycja

class LinkSelectWidget(forms.TextInput):
    template_name = 'widgets/link_select_widget.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['datalist_id'] = f'{name}_datalist'
        context['options'] = [
            '/home/',
            '/aktualnosci/',
            '/o_nas/',
            '/oferta/',
            '/galeria/',
            '/kontakt/',
            '/cennik/',
        ] + [f'/oferta/{obj.slug}/' for obj in Oferta_pozycja.objects.all()]
        return context
