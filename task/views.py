# https://docs.djangoproject.com/en/1.6/ref/request-response/#httpresponse-objects
from django.http import HttpResponse

# http://www.django-rest-framework.org/tutorial/1-serialization#writing-regular-django-views-using-our-serializer
from rest_framework.decorators import api_view

# Allow us to temporarily turn off CSRF check while we test
from django.views.decorators.csrf import csrf_exempt

# http://www.django-rest-framework.org/tutorial/2-requests-and-responses#status-codes
from rest_framework import status

# http://www.django-rest-framework.org/tutorial/2-requests-and-responses#response-objects
from rest_framework.response import Response

# http://www.django-rest-framework.org/tutorial/3-class-based-views
from rest_framework import generics
from rest_framework import mixins

# http://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis
# https://docs.djangoproject.com/en/1.6/topics/http/urls/#reverse-resolution-of-urls
from rest_framework.reverse import reverse

from .serializers import *


# http://www.django-rest-framework.org/api-guide/generic-views#genericapiview
# http://www.django-rest-framework.org/api-guide/generic-views#mixins
# http://www.django-rest-framework.org/api-guide/status-codes

###################################################################
##################### CLASS-BASED VIEWS ###########################
###################################################################
class TaskList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TaskDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CategoryList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TagList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TagDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
###################################################################


###################################################################
##################### FUNCTION-BASED VIEWS ########################
###################################################################
# https://docs.djangoproject.com/en/1.6/topics/http/urls/#reverse-resolution-of-urls
@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'tasks': reverse('task_items', request=request, format=format),
        'categories': reverse('category_items', request=request, format=format),
        'tags': reverse('tag_items', request=request, format=format)
    })


@api_view(['GET', 'POST'])
@csrf_exempt
def tasks(request):
    # https://docs.djangoproject.com/en/dev/ref/request-response/#attributes
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer = TaskSerializer(Task.objects.all().order_by('create_date'), many=True)
    return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
@csrf_exempt
def task_item_by_id(request, pk):
    try:
        task = Task.objects.get(pk=pk)

        if request.method == 'PUT':
            serializer = TaskSerializer(task, data=request.DATA)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            serializer = TaskSerializer(task)
            return Response(serializer.data)
    except Exception as e:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
@csrf_exempt
def categories(request):
    # https://docs.djangoproject.com/en/dev/ref/request-response/#attributes
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer = CategorySerializer(Category.objects.all().order_by('name'), many=True)
    return Response(serializer.data)

@api_view(["GET", "PUT", "DELETE"])
@csrf_exempt
def category_by_id(request, pk):
    try:
        category = Category.objects.get(pk=pk)

        if request.method == 'PUT':
            serializer = CategorySerializer(category, data=request.DATA)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            serializer = CategorySerializer(category)
            return Response(serializer.data)
    except Exception as e:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
@csrf_exempt
def tags(request):
    # https://docs.djangoproject.com/en/dev/ref/request-response/#attributes
    if request.method == 'POST':
        serializer = TagSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer = TagSerializer(Tag.objects.all().order_by('name'), many=True)
    return Response(serializer.data)

@api_view(["GET", "PUT", "DELETE"])
@csrf_exempt
def tag_by_id(request, pk):
    try:
        tag = Tag.objects.get(pk=pk)

        if request.method == 'PUT':
            serializer = TagSerializer(tag, data=request.DATA)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            tag.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            serializer = TagSerializer(tag)
            return Response(serializer.data)
    except Exception as e:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
###################################################################