from django.db import models
from django.conf import settings

from django.core.serializers import serialize

import json

def upload_updata_image(instance, filename):
    return "updata/{user}/{filename}".format(user=instance.user, filename=filename)


class UpdateQuerySet(models.QuerySet):
    # def serialize(self):
    #     qs = self
    #     return serialize('json', qs, fields=('user', 'content', 'image'))
    
    # 아래 방식의 serialize를 가장 추천합니다.
    def serialize(self):
        # qs = self
        list_values = list(self.values("id", "user", "content", "image"))
        return json.dumps(list_values)
    
class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)
    

# Create your models here.
class UpdateModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_updata_image, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    objects = UpdateManager()
    
    def __str__(self):
        return self.content or ""
    
    def serialize(self):
        try:
            image = self.image.url
        except:
            image = ""
        data = {
            "id": self.id,
            "content": self.content,
            "user": self.user.id,
            "image": image
        }
        data = json.dumps(data)
        return data
    

