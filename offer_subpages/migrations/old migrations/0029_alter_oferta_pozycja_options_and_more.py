# Generated by Django 5.2.1 on 2025-05-18 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer_subpages', '0028_alter_oferta_pozycja_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='oferta_pozycja',
            options={'ordering': ['-order'], 'verbose_name': 'Podstrona oferty', 'verbose_name_plural': 'Podstrony oferty'},
        ),
        migrations.RenameField(
            model_name='oferta_pozycja',
            old_name='nazwa',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='oferta_pozycja',
            old_name='kolejnosc',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='oferta_pozycja',
            old_name='tytul',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='link_przycisku',
            new_name='button_link',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='tekst_przycisku',
            new_name='button_text',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='kolor',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='data',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='tekst_pliku',
            new_name='file_text',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='nazwa',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='kolejnosc',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='styl',
            new_name='style',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='tekst',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='tytul',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='post',
            name='plik',
        ),
        migrations.RemoveField(
            model_name='post',
            name='zdjecie',
        ),
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='images/'),
        ),
    ]
