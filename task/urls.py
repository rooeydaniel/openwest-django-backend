"""
https://docs.djangoproject.com/en/1.6/topics/http/urls/

https://zapier.com/learn/apis/chapter-6-api-design/
"""

from django.conf.urls import patterns, url

urlpatterns = patterns('task.views',
    # GET and POST /tasks
    url(r'^tasks$', 'tasks', name="task_items"),

    # GET, PUT and DELETE /tasks/1
    # https://docs.djangoproject.com/en/1.6/topics/http/urls/#named-groups
    url(r'^tasks/(?P<pk>[0-9]+)$', 'task_item_by_id', name="task-item-by-id"),

    # GET and POST /categories
    url(r'^categories$', 'categories', name="category_items"),

    # GET, PUT and DELETE /categories/1
    # https://docs.djangoproject.com/en/1.6/topics/http/urls/#named-groups
    url(r'^categories/(?P<pk>[0-9]+)$', 'category_by_id', name="category-by-id"),

    # GET and POST /tags
    url(r'^tags$', 'tags', name="tag_items"),

    # GET, PUT and DELETE /tags/1
    # https://docs.djangoproject.com/en/1.6/topics/http/urls/#named-groups
    url(r'^tags/(?P<pk>[0-9]+)$', 'tag_by_id', name="tag-by-id"),
)