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
# https://docs.djangoproject.com/en/1.6/topics/db/models/

1. Create the task application
```
    django-admin.py startapp task
```

2. Create your models in the models.py file
```
    from django.db import models


    # https://docs.djangoproject.com/en/1.6/topics/db/models/
    class Task(models.Model):
        class Meta:
            # https://docs.djangoproject.com/en/1.6/ref/models/options/#table-names
            db_table = 'task_task_item'

            # https://docs.djangoproject.com/en/1.6/ref/models/options/#verbose-name-plural
            verbose_name_plural = "task_items"

        # https://docs.djangoproject.com/en/1.6/ref/models/fields/#charfield
        name = models.CharField(max_length=100, null=False, blank=False)

        # https://docs.djangoproject.com/en/1.6/ref/models/fields/#textfield
        description = models.TextField(null=True, blank=True)

        # https://docs.djangoproject.com/en/1.6/ref/models/fields/#integerfield
        priority = models.IntegerField()

        # https://docs.djangoproject.com/en/1.6/ref/models/fields/#datetimefield
        due_date = models.DateTimeField(auto_now=False, auto_now_add=False)

        # https://docs.djangoproject.com/en/1.6/ref/models/fields/#datefield
        create_date = models.DateField(auto_now=False, auto_now_add=True)
        last_modified = models.DateField(auto_now=True, auto_now_add=False)

        # https://docs.djangoproject.com/en/1.6/ref/models/fields/#django.db.models.ForeignKey
        category = models.ForeignKey("Category")

        # https://docs.djangoproject.com/en/1.6/ref/models/fields/#django.db.models.ManyToManyField
        tags = models.ManyToManyField("Tag")

        # https://docs.djangoproject.com/en/1.6/ref/models/instances/#unicode
        def __unicode__(self):
            return self.name


    class Category(models.Model):
        class Meta:
            # https://docs.djangoproject.com/en/1.6/ref/models/options/#verbose-name-plural
            verbose_name_plural = "categories"

        # https://docs.djangoproject.com/en/1.6/ref/models/fields/#charfield
        name = models.CharField(max_length=100, null=False, blank=False)

        # https://docs.djangoproject.com/en/1.6/ref/models/fields/#textfield
        description = models.TextField(null=True, blank=True)

        # https://docs.djangoproject.com/en/1.6/ref/models/instances/#unicode
        def __unicode__(self):
            return self.name


    class Tag(models.Model):
        # https://docs.djangoproject.com/en/1.6/ref/models/fields/#charfield
        name = models.CharField(max_length=100, null=False, blank=False)

        # https://docs.djangoproject.com/en/1.6/ref/models/instances/#unicode
        def __unicode__(self):
            return self.name
```

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
    python manage.py syncdb  # No need to create a super user yet, though you can
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

Django Admin
------------
# https://docs.djangoproject.com/en/1.6/ref/contrib/admin/

1. Update urls.py to account for admin routes
```
    from django.conf.urls import patterns, url, include

    from django.contrib import admin
    admin.autodiscover()

    urlpatterns = patterns('',
        url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
        url(r'^admin/', include(admin.site.urls)),
    )
```

2. Add the admin to the Django apps tuple in settings.py
```
    'django.contrib.admindocs',
    'django.contrib.admin',
```

3. Add docutils library to base requirements files
```
    docutils==0.11
```

4. Install docutils with PIP
5. Register your models to be viewable in admin
```
    from django.contrib import admin
    from .models import *

    # Register your models here.
    admin.site.register(Task)
    admin.site.register(Category)
    admin.site.register(Tag)
```

6. Add static files into settings.py
```
    ########## STATIC FILE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
    STATIC_ROOT = normpath(join(SITE_ROOT, 'staticfiles'))

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
    STATIC_URL = '/static/'

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
    STATICFILES_DIRS = ()

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )
    ########## END STATIC FILE CONFIGURATION
```

7. Add template configuration into settings.py
```
    ########## TEMPLATE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.core.context_processors.tz',
        'django.contrib.messages.context_processors.messages',
        'django.core.context_processors.request',
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
    TEMPLATE_DIRS = ()
    ########## END TEMPLATE CONFIGURATION
```

8. Add static app to Django apps tuple
```
    'django.contrib.staticfiles',
```

9. Synchronize database against two new apps
```
    python manage.py syncdb
```

10. Create a super user
```
    python manage.py createsuperuser
```

11. Log into the admin in your browser - http://localhost:8001/admin/
12. Add some sample data through the admin to your models
13. Take a look at the admin documentation - http://localhost:8001/admin/doc/
14. Apply custom bootstrap theme for the admin, add library to base requirements file
```
    django-admin-bootstrapped==1.6.4
```

15. Add to installed apps in settings file, before admin
```
    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',
```

Django Routes and Function-based Views
--------------------------------------
# https://docs.djangoproject.com/en/1.6/topics/http/urls/

1. Create routes in your task app
```
    from django.conf.urls import patterns, url

    urlpatterns = patterns('task.views',
        # GET and POST /tasks
        url(r'^tasks$', 'tasks', name="tasks"),

        # GET, PUT and DELETE /tasks/1
        url(r'^tasks/(?P<pk>[0-9]+)$', 'task_by_id', name="task-by-id"),

        # GET and POST /categories
        url(r'^categories$', 'categories', name="categories"),

        # GET, PUT and DELETE /tasks/1
        url(r'^categories/(?P<pk>[0-9]+)$', 'category_by_id', name="category-by-id"),

        # GET and POST /priorities
        url(r'^priorities', 'priorities', name="priorities"),

        # GET, PUT and DELETE /tasks/1
        url(r'^priorities/(?P<pk>[0-9]+)$', 'priority_by_id', name="priority-by-id"),
    )
```

2. Include these routes in your main urls file under project
```
    url(r'^', include(task.urls)),
```

3. Create the views for the task routes
```
    from django.views.decorators.http import require_http_methods
    from django.http import HttpResponse
    from django.core import serializers
    from json import dumps

    from .models import *

    @require_http_methods(["GET", "POST"])
    def tasks(request):
        if request.method == 'POST':
            name = request.POST['name'] if request.POST.has_key('name') else None
            description = request.POST['description'] if request.POST.has_key('description') else None
            priority = request.POST['priority'] if request.POST.has_key('priority') else None
            due_date = request.POST['due_date'] if request.POST.has_key('due_date') else None
            category = request.POST['category'] if request.POST.has_key('category') else None
            tags = request.POST['tags'] if request.POST.has_key('tags') else None

            # Should do some validation here

            category = Category.objects.get(pk=category)
            new_task = Task.objects.create(name=name, description=description, priority=priority, due_date=due_date,
                                           category=category)

            tags = tags.split(',')
            for tag in tags:
                new_task.tags.add(Tag.objects.get(pk=tag))

        data = serializers.serialize("json", Task.objects.all().order_by('create_date'))
        return HttpResponse(data, content_type="application/json")

    @require_http_methods(["GET", "PUT", "DELETE"])
    def task_item_by_id(request, pk):
        try:
            task = Task.objects.get(pk=pk)
            data = serializers.serialize("json", [task])

            if request.method == 'PUT':
                print 'The resource was updated!'

            elif request.method == 'DELETE':
                data = serializers.serialize("json", Task.objects.all().order_by('create_date'))
                print 'The resource was deleted!'

            return HttpResponse(data, content_type="application/json")
        except Exception as e:
            return HttpResponse(dumps({'error': 'The resource does not exist'}), content_type="application/json")
```

4. Turn off CSRF Middleware
```
    # 'django.middleware.csrf.CsrfViewMiddleware',
```

5. Test GET and POST RESTful APIs with Postman in Chrome
```
    GET

    http://localhost:8001/task/1

    POST

    name = Test Task Four
    description = Test
    priority = 2
    due_date = 2014-05-09
    category = 2
    tags = 1, 2, 3

    GET

    http://localhost:8001/task/4
```

6. Create the views for the other two resources (category, tags)
```
    @require_http_methods(["GET", "POST"])
    def categories(request):
        if request.method == 'POST':
            name = request.POST['name'] if request.POST.has_key('name') else None
            description = request.POST['description'] if request.POST.has_key('description') else None

            # Should do some validation here

            Category.objects.create(name=name, description=description)

        data = serializers.serialize("json", Category.objects.all().order_by('name'))
        return HttpResponse(data, content_type="application/json")

    @require_http_methods(["GET", "PUT", "DELETE"])
    def category_by_id(request, pk):
        try:
            category = Category.objects.get(pk=pk)
            data = serializers.serialize("json", [category])

            if request.method == 'PUT':
                print 'The resource was updated!'

            elif request.method == 'DELETE':
                data = serializers.serialize("json", Category.objects.all().order_by('name'))
                print 'The resource was deleted!'

            return HttpResponse(data, content_type="application/json")
        except Exception as e:
            return HttpResponse(dumps({'error': 'The resource does not exist'}), content_type="application/json")

    @require_http_methods(["GET", "POST"])
    def tags(request):
        if request.method == 'POST':
            name = request.POST['name'] if request.POST.has_key('name') else None

            # Should do some validation here

            Tag.objects.create(name=name)

        data = serializers.serialize("json", Tag.objects.all().order_by('name'))
        return HttpResponse(data, content_type="application/json")

    @require_http_methods(["GET", "PUT", "DELETE"])
    def tag_by_id(request, pk):
        try:
            tag = Tag.objects.get(pk=pk)
            data = serializers.serialize("json", [tag])

            if request.method == 'PUT':
                print 'The resource was updated!'

            elif request.method == 'DELETE':
                data = serializers.serialize("json", Tag.objects.all().order_by('name'))
                print 'The resource was deleted!'

            return HttpResponse(data, content_type="application/json")
        except Exception as e:
            return HttpResponse(dumps({'error': 'The resource does not exist'}), content_type="application/json")
```

7. Test GET and POST RESTful APIs with Postman in Chrome
```
    GET

    http://localhost:8001/categories

    GET

    http://localhost:8001/categories/1

    POST

    name = Test Category Three
    description = Testing for Test Category Three

    GET

    http://localhost:8001/categories/3

    GET

    http://localhost:8001/tags

    GET

    http://localhost:8001/tags/1

    POST

    name = Test Tag Four

    GET

    http://localhost:8001/tags/4
```