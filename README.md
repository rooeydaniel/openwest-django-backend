===============================================
OpenWest 2014 - Djangular
===============================================

RESTful APIs with Django and AngularJS

Django Project Setup
--------------------
1. Clone front-end project
```
    git clone https://github.com/rooeydaniel/openwest-angular-frontend.git
```

2. Clone back-end project
```
    git clone https://github.com/rooeydaniel/openwest-django-backend.git
```

3. Create and activate virtual environment
4. Install app packages through PIP
5. Run Django's internal server
```
    python manage.py runserver 8001
```

6. Run Node's internal server
```
    node server/server.js
```

7. Open up front-end in your browser - http://localhost:8000/public/index.html
8. Open up back-end in your browser - http://localhost:8001

Django Models
-------------
1. Create the task application
```
    django-admin.py startapp task
```

2. Create your models in the models.py file
3. Update your settings file and add your newly create application
```
    LOCAL_APPS = (
        'task',
    )
```

4. Create a new database for your models in Postgres
```
    createuser -s -P task_manager  # password is T@sk
    createdb -O task_manager djangular
```

5. Update your local_settings.py and add database settings
```
    ########## DATABASE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'djangular',
            'USER': 'task_manager',
            'PASSWORD': 'T@sk',
            'HOST': 'localhost'
        }
    }
    ########## END DATABASE CONFIGURATION
```

6. Add South to your application to handle migrations
```
    THIRD_PARTY_APPS = (
        # http://south.readthedocs.org/en/latest/index.html
        'south',
    )
```

7. Add third-party libraries in base.txt
```
    South==0.8.4
    dj-database-url==0.3.0
    psycopg2==2.5.2
```

8. Install third-party libraries
```
    pip install -r requirements.txt
```

9. Create initial migration
```
    python manage.py schemamigration task --initial
```

10. Synchronize database with models
```
    python manage.py syncdb  # No need to create a super user, we aren't doing authentication
```

11. Run the initial migration
```
    python manage.py migrate task
```

12. Verify the database structure is in place
```
    psql -U task_manager djangular
    djangular=# \dt
```