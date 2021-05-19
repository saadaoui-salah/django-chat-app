from django.urls import re_path

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<root_name>\w+)/$', consumers.ChatRoomConsumer),
]