from django.contrib import admin
from .models import postmodel
# Register your models here.


@admin.register(postmodel)
# disply the post in form of table so requeired to edit 
class adminpostmodel(admin.ModelAdmin):
    list_display=['user','title','language','postedon']
    # search_fields=('user','title','language')
