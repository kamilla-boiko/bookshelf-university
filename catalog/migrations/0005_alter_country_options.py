# Generated by Django 4.1.1 on 2022-09-23 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("catalog", "0004_country_alter_author_country")]

    operations = [
        migrations.AlterModelOptions(
            name="country",
            options={"ordering": ["name"], "verbose_name_plural": "counties"},
        )
    ]
