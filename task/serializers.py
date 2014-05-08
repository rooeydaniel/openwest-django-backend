from rest_framework import serializers

from .models import *

# http://www.django-rest-framework.org/tutorial/1-serialization#using-modelserializers
# http://www.django-rest-framework.org/api-guide/serializers#modelserializer
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task


# http://www.django-rest-framework.org/tutorial/1-serialization#using-modelserializers
# http://www.django-rest-framework.org/api-guide/serializers#modelserializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

# http://www.django-rest-framework.org/tutorial/1-serialization#using-modelserializers
# http://www.django-rest-framework.org/api-guide/serializers#modelserializer
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag