# Bookshelf Project

The Bookshelf project is a Django-based web 
application that allows users to manage a collection 
of books and authors. Users can browse books, search for 
specific titles or authors, view book details, and manage 
author information. The project includes several models, 
views, and forms to provide these functionalities.

## Requirements
* Python 3.x
* Django 3.x
* Pillow (for image handling)

## Installation

```git clone <repository_url>
cd bookshelf_project
python3 -m venv venv
source venv/bin/activate   # On Windows, use "venv\Scripts\activate"
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
You can now access the Bookshelf web application by 
visiting http://127.0.0.1:8000/ in your web browser.

## Usage 

### Django Admin
To access the Django admin interface, go to http://127.0.0.1:8000/admin/ 
and log in using the superuser credentials you created earlier. The admin 
interface allows you to manage Books, Authors, Literary Formats, and Countries. 
You can add, edit, or delete entries through the admin interface.

### Views
The Bookshelf project provides the following views accessible through 
the specified URLs:

* Home Page: http://127.0.0.1:8000/
Displays statistics about the number of books, authors, and the total 
number of visits to the site.
* Book List: http://127.0.0.1:8000/books/
Displays a paginated list of all the books in the database.
Provides a search form to filter books by title and literary format.
Allows users to click on a book to view its details.
* Book Detail: http://127.0.0.1:8000/books/<book_id>/
Shows detailed information about a specific book, including title,
authors, literary format, rate, and an image of the book (if available).
* Book Create: http://127.0.0.1:8000/books/create/
Allows users to create a new book by providing the necessary information in a form.
* Book Update: http://127.0.0.1:8000/books/<book_id>/update/
Allows users to update the information of an existing book.
* Author List: http://127.0.0.1:8000/authors/
Displays a paginated list of all the authors in the database.
Provides a search form to filter authors by last name and country.
Allows users to click on an author to view their details.
* Author Detail: http://127.0.0.1:8000/authors/<author_id>/
Shows detailed information about a specific author, including their
first name, last name, country, birth date, death date, sex, photo, and biography.
Lists all the books authored by the author.
* Author Create: http://127.0.0.1:8000/authors/create/
Allows users to create a new author by providing the necessary information in a form.
* Author Update: http://127.0.0.1:8000/authors/<author_id>/update/
Allows users to update the information of an existing author.
* Genre List: http://127.0.0.1:8000/literary-formats/
Displays a list of all the literary formats available in the database.
* Country List: http://127.0.0.1:8000/countries/
Displays a list of all the countries available in the database.

### Searching and Sorting
The Book List view allows users to search for books based on their 
title and literary format. Additionally, users can sort the books 
by rating (rate) in ascending or descending order.

The Author List view provides a search option to filter authors by 
their last name and country.

##  Conclusion

The Bookshelf project provides a simple and functional web application 
for managing a collection of books and authors. It can be extended and 
customized to suit specific needs, making it a great starting point for 
creating a more comprehensive book management system. Enjoy exploring 
the world of books with the Bookshelf project!
