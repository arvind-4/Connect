from django.contrib import admin

# Register your models here.

from .models import VideoChatRoom

class VideoChatRoomAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created')

admin.site.register(VideoChatRoom, VideoChatRoomAdmin)
# admin.site.register(VideoChatRoomAdmin)