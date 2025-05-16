from django.db import models
from ckeditor.fields import RichTextField


class Footer(models.Model):
    tel = models.CharField("Telefon", max_length=1000, blank=True, null=True)
    mail = models.EmailField("E-mail", max_length=1000, blank=True, null=True)
    adres = models.CharField("Adres", max_length=1000, blank=True, null=True)

    def __str__(self):
        return "Stopka"

    class Meta:
        verbose_name = "stopka"
        verbose_name_plural = "stopka"


# Lista dostępnych styli
STYLE = [
        ('default',     'Tekst, zwykły'),
        ('default-j',   'Tekst, wyjustowany'),
        ('default-c',   'Tekst, wycentrowany'),
        ('wide-panel',  'Tekst, szeroki panel'),
        ('img-left-s',  'Obrazek z lewej, mały'),
        ('img-left-m',  'Obrazek z lewej, średni'),
        ('img-left-l',  'Obrazek z lewej, duży'),
        ('img-right-s', 'Obrazek z prawej, mały'),
        ('img-right-m', 'Obrazek z prawej, średni'),
        ('img-right-l', 'Obrazek z prawej, duży'),
        ('img-top',     'Obrazek na górze'),
        ('img-bot',   'Obrazek na dole'),
    ]

KOLOR = [
    ('kol-bialy',      'Biały'),
    ('kol-szary',      'Szary'),
    ('kol-niebieski',  'Niebieski'),
    ('kol-zielony',    'Zielony'),
    ('kol-rozowy',     'Różowy'),
]


class Page(models.Model):
    nazwa = models.CharField(max_length=1000, blank=True, null=True)
    tytul = models.CharField(max_length=1000, blank=True, null=True)
    tekst = RichTextField(max_length=60000, blank=True, null=True)
    tekst_przycisku = models.CharField(max_length=1000, blank=True, null=True)
    link_przycisku = models.CharField(max_length=1000, blank=True, null=True)
    tekst_pliku = models.CharField(max_length=1000, blank=True, null=True)
    plik = models.FileField(upload_to='pliki/', blank=True, null=True)
    zdjecie = models.ImageField(blank=True, null=True, upload_to='aktualnosci/', max_length=255)
    data = models.DateTimeField(blank=True, null=True)
    styl = models.CharField(max_length=90, choices=STYLE, default='default')
    kolor = models.CharField(max_length=90, choices=KOLOR, default='kol-bialy')
    kolejnosc = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ['kolejnosc']

    def save(self, *args, **kwargs):
        # Jeśli kolejność to 0 lub nieustawiona, ustaw na najwyższą + 1
        if self.kolejnosc == 0:
            # Pobieramy wszystkie obiekty z tej samej klasy
            ModelClass = self.__class__
            max_kolejnosc = ModelClass.objects.aggregate(models.Max('kolejnosc'))['kolejnosc__max'] or 0
            self.kolejnosc = max_kolejnosc + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nazwa or "None"


class Aktualnosci(Page):

    class Meta:
        verbose_name = "aktualności"
        verbose_name_plural = "aktualności"
    

class O_nas(Page):

    class Meta:
        verbose_name = "o nas"
        verbose_name_plural = "o nas"
    

class Oferta(Page):

    class Meta:
        verbose_name = "oferta"
        verbose_name_plural = "oferta"


class Galeria(Page):

    class Meta:
        verbose_name = "galeria"
        verbose_name_plural = "galeria"


class Kontakt(Page):

    class Meta:
        verbose_name = "kontakt"
        verbose_name_plural = "kontakt"


class Cennik(Page):

    class Meta:
        verbose_name = "cennik"
        verbose_name_plural = "cennik"


class Home(Page):

    class Meta:
        verbose_name = "strona domowa"
        verbose_name_plural = "strona domowa"

