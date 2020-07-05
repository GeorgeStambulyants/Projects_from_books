# Projects From Books #

## Preface ##
Here I keep brief overviews of projects from books that I've read or read now.
Each overview may include the following sections:
* Short description of the book.
* Technologies that were used.
* What I have learned from the book.

This file is regularly updated. All finished books are marked.

- - -

## Table of Contents ##

### Algorithms and Data Structures ###
* [__"Algorithms Unlocked"__ -- _Thomas H. Cormen_ | (**FINISHED**)](#algorithms-unlocked-thomas-h-cormen)
* [__"Algorithms"__ -- _Robert Sedgewick and Kevin Wayne_](#algorithms-robert-sedgewick-and-kevin-wayne)

### Django ###
* [__"Building Django Web Applications"__ -- _Tom Aratyn_ | (**FINISHED**)](#building-django-web-applications-tom-aratyn)
* [__"Django 3 By Example"__ -- _Antonio Mele_ | (**FINISHED**)](#django-3-by-example-antonio-mele)
* [__"Django for APIs"__ -- _William S. Vincent_ | (**FINISHED**)](#django-for-apis-william-s-vincent)
* [__"Django for Professionals"__ -- _William S. Vincent_ | (**FINISHED**)](#django-for-professionals-william-s-vincent)
* [__"Django for Beginners"__ -- _William S. Vincent_ | (**FINISHED**)](#django-for-beginners-william-s-vincent)
* [__"Practical Django 2 and Channels 2"__ -- _Frederico Marani_](#practical-django-2-and-channels-2-frederico-marani)

### Flask ###
* [__"Flask By Example"__ -- _Gareth Dwyer_](#flask-by-example-gareth-dwyer)
* [__"Flask Web Development"__ -- _Miguel Grinberg_](#flask-web-development-miguel-grinberg)

### Test-Driven Development ###
* [__"Test-Driven Development with Python"__ -- _Harry J.W. Percival_ | (**FINISHED**)](#test-driven-development-with-python-harry-jw-percival)

### Docker ###
* [__"Using Docker"__ -- _Adrian Mouat_](#using-docker-adrian-mouat)

### DevOps ###
* [__"Python for DevOps"__ -- _Noah Gift, Kennedy Behrman, Alfredo Deza, Grig Cheorghiu_](#python-for-devops-noah-gift)

### JavaScript ###
* [__"JavaScript by Example"__ -- _Dani Akash S_ | (**FINISHED**)](#javascript-by-example-dani-akash-s)

- - -

## Books ##

### ["Algorithms Unlocked", Thomas H. Cormen](https://github.com/GeorgeStambulyants/Projects_from_books/tree/master/Algorithms__Kormen) ###
What I have learned?
- Algorithms for Sorting and Searching
  - Binary search
  - Selection sort
  - Insertion sort
  - Merge sort
  - Quicksort
  - Counting sort
- Directed Acyclic Graphs
  - Topolopical sort
  - Critical path in PERT chart
  - Shortest path in a directed acyclic graph
- Shortest paths
  - Dijkstra's algorithm
  - The Bellman-Ford algorithm
  - The Floyd-Warshall algorithm
- Algorithms on Strings
  - Longest common subsequence
- Foundations of Cryprography
- Data Compression

- - -

### "Algorithms", Robert Sedgewick and Kevin Wayne ###
editing...

- - -

### ["Building Django Web Applications", Tom Aratyn](https://github.com/GeorgeStambulyants/Projects_from_books/tree/master/Django__Aratyn) ###
Over the course of this book 3 projects were built

#### [MyMDB](https://github.com/GeorgeStambulyants/Projects_from_books/tree/master/Django__Aratyn/MyMDB) ####
MyMDB is a basic Internet Movie Database (IMDB) clone.

__In this web application I have learned about__:
* Django basics
* Caching and Django's caching API
* OWASP top 10 list or risks and how Django can help mitigate them

__Python libs I worked with__:
* django
* pillow
* psycopg2
* django-debug-toolbar

#### [answerly](https://github.com/GeorgeStambulyants/Projects_from_books/tree/master/Django__Aratyn/answerly)
Answerly is a Stack Overflow clone.

__In this web application I have learned about__:
* CRUD
* Elasticsearch
* Testing Django projects

__Python libs I worked with__ (libraries, that are the same as in MyMDB project are omitted):
* coverage
* django-crispy-forms
* django-markdownify
* elasticsearch
* facroty-boy
* markdown
* selenium

#### [mailape](https://github.com/GeorgeStambulyants/Projects_from_books/tree/master/Django__Aratyn/mailape) ####
Mail Ape is a mailing list manager that will let users start mailing lists, sign up for mailing 
lists, and then message people.

__In this web application I have learned about__:
* How to use celery
* An API and how to build it with Django
* Redis

__Python libs I worked with__ (libraries, that are the same as in MyMDB and answerly projects are omitted):
* celery
* django-celery-results
* django_rest_framework
* redis

- - -

### ["Django 3 By Example", Antonio Mele](https://github.com/GeorgeStambulyants/Projects_from_books/tree/master/Django__Mele) ###
Over the course of this book 4 projects were built

#### [Blog](https://github.com/GeorgeStambulyants/Projects_from_books/tree/master/Django__Mele/Blog) ####
Simple Blog application in Django.

__In this web application I have learned about__:
* Django basics
* Sitemaps
* RSS feeds

__Python libs I worked with__:
* django
* django-taggit
* markdown

#### [Bookmarks](https://github.com/GeorgeStambulyants/Projects_from_books/tree/master/Django__Mele/Bookmarks) ####
Bookmarks is a simple socail application


__In this web application I have learned about__:
* Authentication and how it can be implemented in Django
* jQuery basics
* AJAX
* Django signals
* Redis

__Python libs I worked with__(libraries, that are the same as in Blog project are omitted):
* oauthlib
* pillow
* redis
* sorl-thumbnail
* social-auth-app-django

#### [Shop](https://github.com/GeorgeStambulyants/Projects_from_books/tree/master/Django__Mele/Shop) ####
This project is a fully featured online shop

__In this web application I have learned about__:
* Django sessions
* Launching asynchronous tasks with Celery
* RabbitMQ
* Integrating a payment gateway
* Generating PDFs
* Internationalization and localization

__Python libs I worked with__(libraries, that are the same as in Blog and Bookmarks projects are omitted):
* braintree
* celery
* django-localflavor
* django-parler
* django-rosetta
* flower
* WeasyPrint
* Pyphen

#### [E-Learning Platform](https://github.com/GeorgeStambulyants/Projects_from_books/tree/master/Django__Mele/E-Learning_Platform) ####
This project is a E-Learning Platform with content management system (CMS)

__In this web application I have learned about__:
* CMS and how it can be implemented with Django
* Caching and Django-s caching API
* Memcached
* RESTful API and how it can be implemented in Django
* Django Channels

__Python libs I worked with__(libraries, that are the same as in Blog, Shop and Bookmarks projects are omitted):
* channels
* channels-redis
* django-braces
* django_rest_framework
* python-memcached

- - -

### "Django for APIs", William S. Vincent ###
editing...

- - -

### "Django for Professionals", William S. Vincent ###
editing...

- - -

### "Django for Beginners", William S. Vincent ###
editing...

- - -

### "Practical Django 2 and Channels 2", Frederico Marani ###
editing...

- - -

### "Flask By Example", Gareth Dwyer ###
editing...

- - -

### "Flask Web Development", Miguel Grinberg ###
editing...

- - -

### "Test-Driven Development with Python", Harry J.W. Percival ###
editing...

- - -

### "Using Docker", Adrian Mouat ###
editing...

- - -

### "Python for DevOps", Noah Gift ###
edititg

- - -

### "JavaScript by Example", Dani Akash S ###
editing...

- - -
