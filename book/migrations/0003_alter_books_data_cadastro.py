# Generated by Django 4.1.1 on 2022-09-20 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_books_options_alter_books_co_autor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='data_cadastro',
            field=models.DateField(auto_now=True),
        ),
    ]
