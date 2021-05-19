from django.shortcuts import render

def index(request):


    context  = {}
    return render(request, "index.html", context)

def room(request, room_name):
    context  = {"room_name":room_name}
    return render(request, "chatroom.html", context)

