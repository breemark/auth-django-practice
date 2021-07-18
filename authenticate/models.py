from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    fav_color = models.CharField(max_length=120, null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.user.delete()
        return super(self.__class__, self).delete(*args, **kwargs)