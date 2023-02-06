from django.shortcuts import render
from . models import CustomUser

def users_info(request):
    users = list(CustomUser.objects.all().values())
    context = {'users': users}
    return render(request, "users_info.html", context)

def user_info(request, id):
    user = CustomUser.objects.get(id=id)
    context = {'user': user}
    return render(request, "user_info.html", context)


