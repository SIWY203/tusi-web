from django.db import models
from django.utils.text import slugify
from tusi.models import Page

class OfferItem(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Podstrona oferty"
        verbose_name_plural = "Podstrony oferty"
        ordering = ['-order']

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while OfferItem.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name or f"Oferta {self.id}"


class Post(Page):
    offer_item = models.ForeignKey(OfferItem, related_name="posts", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Zawartość podstrony"
        verbose_name_plural = "Zawartość podstron"

    