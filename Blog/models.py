from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE, DO_NOTHING
from ckeditor.fields import RichTextField

# Create your models here.
user= settings.AUTH_USER_MODEL

# post form for posting 
class postmodel(models.Model):
    user = models.ForeignKey(user,on_delete=CASCADE,default=1)    # user whose post it id 
    title = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    des = RichTextField()
    code = RichTextField()
    postedon = models.DateField(auto_now=True)

    


    