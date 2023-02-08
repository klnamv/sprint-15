from django.shortcuts import render, redirect
from . models import CustomUser
from book.views import book_list
from django.contrib.auth import authenticate, login, logout


def users_info(request):

    users = list(CustomUser.objects.filter(role=0).values())
    context = {'users': users}
    return render(request, "users_info.html", context)


def user_info(request, id):
    user = CustomUser.objects.get(id=id)
    context = {'user': user}
    return render(request, "user_info.html", context)


def log_in(request):
    print(request.user)
    context = {}
    if request.method == 'POST':
        user = CustomUser.get_by_email(request.POST['email'])
        if user is None:
            context['Error_message'] = 'user not found'
        else:
            if user.password != request.POST['password']:
                context['Error_message'] = 'incorrect password'
            else:
                login(request, user)
                user.is_active = True
                user.save()
                return redirect('book:book_list')
    return render(request, 'log_in.html', context)


def sign_up(request):
    print(request.POST)
    context = {}
    if request.method == 'POST':
        print(request.POST['f_name'])
        if request.POST['password'] != request.POST['password2']:
            context['Error_message'] = 'different password'
        else:
            if request.POST.get('is_admin') == 'on':
                is_admin = True
            else:
                is_admin = False

            new_user = CustomUser.create(request.POST['email'], request.POST['password'],
                                         request.POST['f_name'], request.POST['m_name'],
                                         request.POST['l_name'])
            new_user.update(role=int(is_admin))

    return render(request, 'sign_up.html', context)

def log_out(request):
    logout(request)
    return redirect('auth:log_in')