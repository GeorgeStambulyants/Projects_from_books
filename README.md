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
In this book I have learned how to build multiple RESTful APIs. Three projects were built using Django and Django Rest Framework.

#### [library](https://github.com/GeorgeStambulyants/Projects_from_books/tree/master/Django_for_APIs__Vincent/library) ####
This is a simple basic library website, that was extended into a web API with Django REST Framework.

#### [todo API](https://github.com/GeorgeStambulyants/Projects_from_books/tree/master/Django_for_APIs__Vincent/todo) ####
In this project a simple Todo API back-end was built. Then it was connected with a React front-end

__Additional Python libs__:
* django-cors-headers

#### [Blog API](https://github.com/GeorgeStambulyants/Projects_from_books/tree/master/Django_for_APIs__Vincent/blogapi) ####
In this project full set of Django REST Framework features were used. This application has users, permissions and allows for full CRUD functionality.

__Additional Python libs__
* django-rest-auth
* django-allauth

- - -

### ["Django for Professionals", William S. Vincent](https://github.com/GeorgeStambulyants/Projects_from_books/tree/master/Django_for_Professionals__Vincent/) ###
In this book Bookstore project was built.

__In this web application I have learned about__:
* Docker and how it can be used during development and production with Django
* Docker-compose
* Static assets and how to manage them in Django project
* Integrating a payment gateway
* Measuring performance in Django project
* Security in Django projects
* Deployment with Heroku
* And a lot of other insteresting Django stuff

__Python libs I worked with__:
* django-all-auth
* pillow
* stripe
* django-debug-toolbar
* whitenoise
* gunicorn
* dj-database-url
* django-crispy-forms

- - -

### ["Django for Beginners", William S. Vincent](https://github.com/GeorgeStambulyants/Projects_from_books/tree/master/Django_for_Beginners__Vincent/) ###
Nothing interesting here. Just four small simple Django projects to learn the basics.

- - -

### ["Practical Django 2 and Channels 2", Frederico Marani](https://github.com/GeorgeStambulyants/Projects_from_books/tree/master/Django__Marani) ###
Coming soon... Book is not finished.

- - -

### ["Flask By Example", Gareth Dwyer](https://github.com/GeorgeStambulyants/Projects_from_books/tree/master/Flask__Dwyer) ###
This book taught me the basics of the Flask Web Framework. Two projects were built

#### [Headlines Project](https://github.com/GeorgeStambulyants/Projects_from_books/tree/master/Flask__Dwyer/headlines) ####
Headlines application displays up-to-date news headlines, weather information and currency exchange.

__In this web application I have learned about__:
* Flask basics
* Using RSS feeds from Python
* Working with different APIs
* Deployment on VPS

#### [Crimemap project](https://github.com/GeorgeStambulyants/Projects_from_books/tree/master/Flask__Dwyer/crimemap) ####
Crimemap is an interactive crime map that allows to tag locations with details of witnessed or experienced criminal activities

__In this web application I have learned about__:
* MySQL and how to work with it from Python
* Deployment on VPS
* Security in Flask applications
* Working with different APIs
* Using static assets in Flask application

- - -

### ["Flask Web Development", Miguel Grinberg](https://github.com/GeorgeStambulyants/Projects_from_books/tree/master/Flask__Grinberg) ###
Comming soon... Book is not finished.
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
