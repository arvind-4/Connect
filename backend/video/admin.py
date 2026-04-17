"""Admin for the video chat room."""

from django.contrib import admin

from backend.video.models import VideoChatRoom


class VideoChatRoomAdmin(admin.ModelAdmin):
    """Admin for the video chat room."""

    list_display = ("__str__", "created")


admin.site.register(VideoChatRoom, VideoChatRoomAdmin)
