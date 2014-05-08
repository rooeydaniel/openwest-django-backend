# https://docs.djangoproject.com/en/1.6/topics/http/decorators/#allowed-http-methods
from django.views.decorators.http import require_http_methods

# https://docs.djangoproject.com/en/1.6/ref/request-response/#httpresponse-objects
from django.http import HttpResponse

# https://docs.djangoproject.com/1.6/dev/topics/serialization/
from django.core import serializers

# https://docs.python.org/2/library/json.html
from json import dumps

from .models import *

@require_http_methods(["GET", "POST"])
def tasks(request):
    # https://docs.djangoproject.com/en/dev/ref/request-response/#attributes
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