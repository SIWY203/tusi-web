from django.db import models
from django.utils.text import slugify
from tusi.models import Page

class Oferta_pozycja(models.Model):
    nazwa = models.CharField(max_length=1000, blank=True, null=True)
    tytul = models.CharField(max_length=1000, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    kolejnosc = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Podstrona oferty"
        verbose_name_plural = "Podstrony oferty"
        ordering = ['-kolejnosc']

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.tytul)
            slug = base_slug
            counter = 1
            while Oferta_pozycja.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nazwa or f"Oferta {self.id}"


class Post(Page):
    oferta_pozycja = models.ForeignKey(Oferta_pozycja, related_name="posts", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Zawartość podstrony"
        verbose_name_plural = "Zawartość podstron"

    