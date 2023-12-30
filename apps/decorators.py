from django.http import HttpResponse
from django.shortcuts import redirect

def gohome_if_authenticated(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            role = request.user.role
            #for group in request.user.groups.all():
            #   user_groups.append(group.name)
            if role in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not allowed to view this page")
        return wrapper_func
    return decorator

def disallowed_users(disallowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            role = request.user.role
            #for group in request.user.groups.all():
            #   user_groups.append(group.name)
            if role in disallowed_roles:
                return HttpResponse("You are not allowed to view this page")
            else:
                return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator