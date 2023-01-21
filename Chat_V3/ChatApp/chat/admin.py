from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from.models import Room,Message



class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}
    
class MessageAdmin(admin.ModelAdmin):
    list_display = ('room', 'content','user')
    list_filter = ('room', 'content','user')
    search_fields = ('room', 'content','user')
    

    
    
admin.site.register(Room,RoomAdmin)
admin.site.register(Message,MessageAdmin)


