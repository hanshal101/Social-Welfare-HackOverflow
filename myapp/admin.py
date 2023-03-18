from django.contrib import admin
from .models import News, Updates   
from .models import Room, Message 
# Register your models here.
admin.site.register(News)
admin.site.register(Updates)
admin.site.register(Room)
admin.site.register(Message)