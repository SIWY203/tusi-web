# Generated by Django 5.2.1 on 2025-05-18 15:18

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tusi', '0051_rename_mail_footer_email_rename_tel_footer_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('text', ckeditor.fields.RichTextField(blank=True, max_length=60000, null=True)),
                ('button_text', models.CharField(blank=True, max_length=1000, null=True)),
                ('button_link', models.CharField(blank=True, max_length=1000, null=True)),
                ('file_text', models.CharField(blank=True, max_length=1000, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='files/')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='images/')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('style', models.CharField(choices=[('default', 'Tekst, zwykły'), ('default-j', 'Tekst, wyjustowany'), ('default-c', 'Tekst, wycentrowany'), ('wide-panel', 'Tekst, szeroki panel'), ('img-left-s', 'Obrazek z lewej, mały'), ('img-left-m', 'Obrazek z lewej, średni'), ('img-left-l', 'Obrazek z lewej, duży'), ('img-right-s', 'Obrazek z prawej, mały'), ('img-right-m', 'Obrazek z prawej, średni'), ('img-right-l', 'Obrazek z prawej, duży'), ('img-top', 'Obrazek na górze'), ('img-bot', 'Obrazek na dole')], default='default', max_length=90)),
                ('color', models.CharField(choices=[('kol-bialy', 'Biały'), ('kol-szary', 'Szary'), ('kol-niebieski', 'Niebieski'), ('kol-zielony', 'Zielony'), ('kol-rozowy', 'Różowy')], default='kol-bialy', max_length=90)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'O nas',
                'verbose_name_plural': 'O nas',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('text', ckeditor.fields.RichTextField(blank=True, max_length=60000, null=True)),
                ('button_text', models.CharField(blank=True, max_length=1000, null=True)),
                ('button_link', models.CharField(blank=True, max_length=1000, null=True)),
                ('file_text', models.CharField(blank=True, max_length=1000, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='files/')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='images/')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('style', models.CharField(choices=[('default', 'Tekst, zwykły'), ('default-j', 'Tekst, wyjustowany'), ('default-c', 'Tekst, wycentrowany'), ('wide-panel', 'Tekst, szeroki panel'), ('img-left-s', 'Obrazek z lewej, mały'), ('img-left-m', 'Obrazek z lewej, średni'), ('img-left-l', 'Obrazek z lewej, duży'), ('img-right-s', 'Obrazek z prawej, mały'), ('img-right-m', 'Obrazek z prawej, średni'), ('img-right-l', 'Obrazek z prawej, duży'), ('img-top', 'Obrazek na górze'), ('img-bot', 'Obrazek na dole')], default='default', max_length=90)),
                ('color', models.CharField(choices=[('kol-bialy', 'Biały'), ('kol-szary', 'Szary'), ('kol-niebieski', 'Niebieski'), ('kol-zielony', 'Zielony'), ('kol-rozowy', 'Różowy')], default='kol-bialy', max_length=90)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Kontakt',
                'verbose_name_plural': 'Kontakt',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('text', ckeditor.fields.RichTextField(blank=True, max_length=60000, null=True)),
                ('button_text', models.CharField(blank=True, max_length=1000, null=True)),
                ('button_link', models.CharField(blank=True, max_length=1000, null=True)),
                ('file_text', models.CharField(blank=True, max_length=1000, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='files/')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='images/')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('style', models.CharField(choices=[('default', 'Tekst, zwykły'), ('default-j', 'Tekst, wyjustowany'), ('default-c', 'Tekst, wycentrowany'), ('wide-panel', 'Tekst, szeroki panel'), ('img-left-s', 'Obrazek z lewej, mały'), ('img-left-m', 'Obrazek z lewej, średni'), ('img-left-l', 'Obrazek z lewej, duży'), ('img-right-s', 'Obrazek z prawej, mały'), ('img-right-m', 'Obrazek z prawej, średni'), ('img-right-l', 'Obrazek z prawej, duży'), ('img-top', 'Obrazek na górze'), ('img-bot', 'Obrazek na dole')], default='default', max_length=90)),
                ('color', models.CharField(choices=[('kol-bialy', 'Biały'), ('kol-szary', 'Szary'), ('kol-niebieski', 'Niebieski'), ('kol-zielony', 'Zielony'), ('kol-rozowy', 'Różowy')], default='kol-bialy', max_length=90)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Galeria',
                'verbose_name_plural': 'Galerie',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('text', ckeditor.fields.RichTextField(blank=True, max_length=60000, null=True)),
                ('button_text', models.CharField(blank=True, max_length=1000, null=True)),
                ('button_link', models.CharField(blank=True, max_length=1000, null=True)),
                ('file_text', models.CharField(blank=True, max_length=1000, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='files/')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='images/')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('style', models.CharField(choices=[('default', 'Tekst, zwykły'), ('default-j', 'Tekst, wyjustowany'), ('default-c', 'Tekst, wycentrowany'), ('wide-panel', 'Tekst, szeroki panel'), ('img-left-s', 'Obrazek z lewej, mały'), ('img-left-m', 'Obrazek z lewej, średni'), ('img-left-l', 'Obrazek z lewej, duży'), ('img-right-s', 'Obrazek z prawej, mały'), ('img-right-m', 'Obrazek z prawej, średni'), ('img-right-l', 'Obrazek z prawej, duży'), ('img-top', 'Obrazek na górze'), ('img-bot', 'Obrazek na dole')], default='default', max_length=90)),
                ('color', models.CharField(choices=[('kol-bialy', 'Biały'), ('kol-szary', 'Szary'), ('kol-niebieski', 'Niebieski'), ('kol-zielony', 'Zielony'), ('kol-rozowy', 'Różowy')], default='kol-bialy', max_length=90)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Aktualność',
                'verbose_name_plural': 'Aktualności',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('text', ckeditor.fields.RichTextField(blank=True, max_length=60000, null=True)),
                ('button_text', models.CharField(blank=True, max_length=1000, null=True)),
                ('button_link', models.CharField(blank=True, max_length=1000, null=True)),
                ('file_text', models.CharField(blank=True, max_length=1000, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='files/')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='images/')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('style', models.CharField(choices=[('default', 'Tekst, zwykły'), ('default-j', 'Tekst, wyjustowany'), ('default-c', 'Tekst, wycentrowany'), ('wide-panel', 'Tekst, szeroki panel'), ('img-left-s', 'Obrazek z lewej, mały'), ('img-left-m', 'Obrazek z lewej, średni'), ('img-left-l', 'Obrazek z lewej, duży'), ('img-right-s', 'Obrazek z prawej, mały'), ('img-right-m', 'Obrazek z prawej, średni'), ('img-right-l', 'Obrazek z prawej, duży'), ('img-top', 'Obrazek na górze'), ('img-bot', 'Obrazek na dole')], default='default', max_length=90)),
                ('color', models.CharField(choices=[('kol-bialy', 'Biały'), ('kol-szary', 'Szary'), ('kol-niebieski', 'Niebieski'), ('kol-zielony', 'Zielony'), ('kol-rozowy', 'Różowy')], default='kol-bialy', max_length=90)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Oferta',
                'verbose_name_plural': 'Oferty',
            },
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('text', ckeditor.fields.RichTextField(blank=True, max_length=60000, null=True)),
                ('button_text', models.CharField(blank=True, max_length=1000, null=True)),
                ('button_link', models.CharField(blank=True, max_length=1000, null=True)),
                ('file_text', models.CharField(blank=True, max_length=1000, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='files/')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='images/')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('style', models.CharField(choices=[('default', 'Tekst, zwykły'), ('default-j', 'Tekst, wyjustowany'), ('default-c', 'Tekst, wycentrowany'), ('wide-panel', 'Tekst, szeroki panel'), ('img-left-s', 'Obrazek z lewej, mały'), ('img-left-m', 'Obrazek z lewej, średni'), ('img-left-l', 'Obrazek z lewej, duży'), ('img-right-s', 'Obrazek z prawej, mały'), ('img-right-m', 'Obrazek z prawej, średni'), ('img-right-l', 'Obrazek z prawej, duży'), ('img-top', 'Obrazek na górze'), ('img-bot', 'Obrazek na dole')], default='default', max_length=90)),
                ('color', models.CharField(choices=[('kol-bialy', 'Biały'), ('kol-szary', 'Szary'), ('kol-niebieski', 'Niebieski'), ('kol-zielony', 'Zielony'), ('kol-rozowy', 'Różowy')], default='kol-bialy', max_length=90)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Cennik',
                'verbose_name_plural': 'Cenniki',
            },
        ),
        migrations.DeleteModel(
            name='Aktualnosci',
        ),
        migrations.DeleteModel(
            name='Cennik',
        ),
        migrations.DeleteModel(
            name='Galeria',
        ),
        migrations.DeleteModel(
            name='Kontakt',
        ),
        migrations.DeleteModel(
            name='O_nas',
        ),
        migrations.DeleteModel(
            name='Oferta',
        ),
        migrations.AlterModelOptions(
            name='home',
            options={'verbose_name': 'Główna', 'verbose_name_plural': 'Główne'},
        ),
        migrations.RenameField(
            model_name='home',
            old_name='link_przycisku',
            new_name='button_link',
        ),
        migrations.RenameField(
            model_name='home',
            old_name='tekst_przycisku',
            new_name='button_text',
        ),
        migrations.RenameField(
            model_name='home',
            old_name='kolor',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='home',
            old_name='data',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='home',
            old_name='tekst_pliku',
            new_name='file_text',
        ),
        migrations.RenameField(
            model_name='home',
            old_name='nazwa',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='home',
            old_name='kolejnosc',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='home',
            old_name='styl',
            new_name='style',
        ),
        migrations.RenameField(
            model_name='home',
            old_name='tekst',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='home',
            old_name='tytul',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='home',
            name='plik',
        ),
        migrations.RemoveField(
            model_name='home',
            name='zdjecie',
        ),
        migrations.AddField(
            model_name='home',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
        migrations.AddField(
            model_name='home',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='images/'),
        ),
    ]
