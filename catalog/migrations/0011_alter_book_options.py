# Generated by Django 4.1.1 on 2022-09-23 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("catalog", "0010_alter_book_options")]

    operations = [
        migrations.AlterModelOptions(name="book", options={"ordering": ["title"]})
    ]
