"""
https://docs.djangoproject.com/en/1.6/topics/http/urls/

https://zapier.com/learn/apis/chapter-6-api-design/
"""
from django.conf.urls import patterns, url

from .views import TaskList, TaskDetail, CategoryList, CategoryDetail, TagList, TagDetail

urlpatterns = patterns('task.views',
    url(r'^$', 'api_root', name="api-root"),

    # GET and POST /tasks
    # url(r'^tasks$', 'tasks', name="task_items"),  # function-based view
    url(r'^tasks$', TaskList.as_view(), name="task_items"),  # class-based view

    # GET, PUT and DELETE /tasks/1
    # https://docs.djangoproject.com/en/1.6/topics/http/urls/#named-groups
    # url(r'^tasks/(?P<pk>[0-9]+)$', 'task_item_by_id', name="task-item-by-id"),  # function-based view
    url(r'^tasks/(?P<pk>[0-9]+)$', TaskDetail.as_view(), name="task-item-by-id"),  # class-based view

    # GET and POST /categories
    # url(r'^categories$', 'categories', name="category_items"),  # function-based view
    url(r'^categories$', CategoryList.as_view(), name="category_items"),  # class-based view

    # GET, PUT and DELETE /categories/1
    # https://docs.djangoproject.com/en/1.6/topics/http/urls/#named-groups
    # url(r'^categories/(?P<pk>[0-9]+)$', 'category_by_id', name="category-by-id"),  # function-based view
    url(r'^categories/(?P<pk>[0-9]+)$', CategoryDetail.as_view(), name="category-by-id"),  # class-based view

    # GET and POST /tags
    # url(r'^tags$', 'tags', name="tag_items"),  # function-based view
    url(r'^tags$', TagList.as_view(), name="tag_items"),  # class-based view

    # GET, PUT and DELETE /tags/1
    # https://docs.djangoproject.com/en/1.6/topics/http/urls/#named-groups
    # url(r'^tags/(?P<pk>[0-9]+)$', 'tag_by_id', name="tag-by-id"),  # function-based view
    url(r'^tags/(?P<pk>[0-9]+)$', TagDetail.as_view(), name="tag-by-id"),  # class-based view
)