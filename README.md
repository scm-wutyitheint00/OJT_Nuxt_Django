# Nuxt + Django OJT

## Requirements
 - [Python3](https://www.python.org/)
 - [Django](https://pypi.org/project/Django/)
 - [Nuxt](https://nuxtjs.org/)
 
## Django Libraries
  - [Django rest framework](https://pypi.org/project/djangorestframework/) for authentication with token
  - [Django filter](https://pypi.org/project/django-filter/) for search filter
  - [CORS header](https://pypi.org/project/django-cors-headers/) for cors whitelists
  - Default sqlite3 for database
  
## Nuxt Libraries
  - [Vuetify](https://www.npmjs.com/package/vuetify) for UI components
  - [Nuxtjs Auth](https://www.npmjs.com/package/@nuxtjs/auth) for authentication
  - [Axios](https://www.npmjs.com/package/@nuxtjs/axios) for http interceptor
  
## Configuring the Backend
 1. navigate to `django_side`
 2. run `pip install -r requirements.txt` to install all dependencies
 3. run `python manage.py migrate` to create the database
 4. create a superuser with `python manage.py createsuperuser`
 5. start server with`python manage.py runserver`
 6. login using your admin credentials `localhost:8000/admin` to check admin dashboard (optional)
  
## Configuring the Frontend 
 1. navigate to `nuxt_side` and `npm install`
 2. start the server with `npm run dev`
 3. you may go back to `localhost:3000`
 4. register and login to check the functions
 

