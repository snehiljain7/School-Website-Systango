from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrappper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('adminhome')
        else:
            return view_func(request,*args, **kwargs)
    return wrappper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrappper_func(request,*args, **kwargs):
            group = None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request,*args, **kwargs)
            else:
                return HttpResponse("you are not authorised to view this page")
        return wrappper_func
    return decorator

def admin_only(view_func):
        def wrappper_func(request,*args, **kwargs):
            group = None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name

            if group == 'student':
                return redirect('studentDash')
            if group == 'teacher':
                return redirect('teacherDash')
            if group =='admin':
                return view_func(request,*args, **kwargs)
        return wrappper_func
