TCM is a Django app. You will need Python 2.6 as well as the 'couchdb' and 'django' Python modules installed. Then you can set the app up:

python manage.py syncdb

This will initialize the CouchDB views and databases

python manage.py runserver

This will start the Django development server. Now you can view the app:

http://localhost:8000/tcm/

