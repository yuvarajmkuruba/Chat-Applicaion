from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import *
# Register your models here.
class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)
admin.site.register(Video)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Feature)