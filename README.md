# django-rest-framework

```
Python==2.7.13
Django==1.10.6
```

Tutorial for django rest framework from official site. 
http://www.django-rest-framework.org/tutorial/quickstart/

Install PostgreSQL database:
```
sudo apt-get install postgresql libpq-dev
sudo -u postgres psql
CREATE USER tutorial WITH PASSWORD 'tutorial';
ALTER USER tutorial CREATEDB;
CREATE DATABASE tutorial WITH OWNER tutorial;
```

To make migration get into **/tutorial/** directory and use:
```
python manage.py migrate
```

To run application get into **/tutorial/** directory and use:
```
python manage.py runserver
```
