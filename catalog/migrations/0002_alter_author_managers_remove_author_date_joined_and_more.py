# Generated by Django 4.1.1 on 2022-09-20 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("catalog", "0001_initial")]

    operations = [
        migrations.AlterModelManagers(name="author", managers=[]),
        migrations.RemoveField(model_name="author", name="date_joined"),
        migrations.RemoveField(model_name="author", name="email"),
        migrations.RemoveField(model_name="author", name="groups"),
        migrations.RemoveField(model_name="author", name="is_active"),
        migrations.RemoveField(model_name="author", name="is_staff"),
        migrations.RemoveField(model_name="author", name="is_superuser"),
        migrations.RemoveField(model_name="author", name="last_login"),
        migrations.RemoveField(model_name="author", name="password"),
        migrations.RemoveField(model_name="author", name="user_permissions"),
        migrations.RemoveField(model_name="author", name="username"),
        migrations.AlterField(
            model_name="author",
            name="birth_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="author",
            name="death_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="author",
            name="first_name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="author",
            name="last_name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="author",
            name="photo",
            field=models.ImageField(upload_to="photos/"),
        ),
        migrations.AlterField(
            model_name="book",
            name="authors",
            field=models.ManyToManyField(related_name="books", to="catalog.author"),
        ),
        migrations.AlterField(
            model_name="book",
            name="image",
            field=models.ImageField(upload_to="images/"),
        ),
    ]
