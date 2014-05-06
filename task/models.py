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