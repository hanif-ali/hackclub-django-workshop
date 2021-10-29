# NUSTBoard - Demo Project
*Demo Project for HackClub's Django Workshop*

This demo project is to help understand the basic concepts of Django and how they tie together to build a web application.

## Requirements
- Python 3.6+
- Django 3+

## How to Run
With Django and Python installed, go to the `nustboard` directory and run:
```
$ python manage.py makemigrations
```
After that run:
```
$ Python manage.py migrate
```

This would set up the database tables. Once done, you can run the development server using:
```
$ python manage.py runserver
```