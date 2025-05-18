from django.contrib import admin
from django import forms
from .models import OfferItem, Post
from tusi.admin import BasePageAdmin


# Hide slug from the form
class OfferItemForm(forms.ModelForm):
    class Meta:
        model = OfferItem
        exclude = ('slug',)


class OfferItemAdmin(BasePageAdmin):
    form = OfferItemForm
    list_display = ['name', 'slug', 'order']
    list_editable = ['order']
    ordering = ['order']


class PostAdmin(BasePageAdmin):
    list_display = ['offer_item', 'name', 'style', 'color', 'order']
    search_fields = ('name',)
    list_editable = ['style', 'color', 'order']
    list_display_links = ('name',)
    ordering = ['order']
    list_filter = ['offer_item']


admin.site.register(Post, PostAdmin)
admin.site.register(OfferItem, OfferItemAdmin)
