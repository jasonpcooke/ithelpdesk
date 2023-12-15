# Service Desk App
## For Software Engineering & Agile
This app is designed to provide simple functions around CRUD of a database. The app itself is a 'service desk'- users can raise issues around their devices, and admins will be able to change the status of these issues depending on their status.
## Pre-requisites
App was built using python 3.9.  
Django is the chosen framework; this project was built using 4.2.6.  
Unittest is used for unit testing. This is supported and included with django.  
sqlite is used for database.  This is supported and included with python.  
## Starting the app
### 1. Build
To generate the database, run these commands a line at a time in your terminal at the root of the project:  
  
`python manage.py sqlmigrate helpdeskapplication 0001`  
  
`python manage.py migrate`

And finally, to populate the user table with an admin:  

`python manage.py createsuperuser`  

follow the prompts in terminal to create a super user.  
  
### 2. Starting the application
in terminal, run  
  
  `python manage.py runserver`  
    
and head to the URL http://127.0.0.1:8000/helpdeskapplication/login .  
Use the super user details entered in terminal to access the admin rest screen, provided by django's rest API.  

In here, you can interact with the relevant tables for the application.

Click change on the Persons table, open up your super user details and copy the encrypted password.  
  
Next, add a new Person to the Persons table. Here, you can enter an email, firstname and surname, and paste that previously used password into the password box. Finally, tick is active and is staff, and save the record.  
  
With this new user, you should now be able to access the site. Click view site in the top right of the webpage to return to the login page. This time, enter the email of the new user and the password of  your first user.  

Welcome to the dashboard! Feel free to play around as you please.