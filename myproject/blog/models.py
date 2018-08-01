from django.db import models

# Create your models here.


from django.db import models
from django.conf import settings

class Post(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title