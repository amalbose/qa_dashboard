from django.shortcuts import render

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from qa_dashboard import common

from .forms import UserForm, UserProfileForm

def home(request):
    context = {
    "title" : "Project Admin"
    }
    return render(request,"home.html" , context);


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print (user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context = {
               'user_form': user_form, 
               'profile_form': profile_form, 
               'registered': registered
               }
    return render( request, 'register.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                auth_login(request, user)
                if "login" not in request.META.get('HTTP_REFERER'):
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                else:
                    return HttpResponseRedirect("/")
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'login.html', { 'title' : common.APPLICATION_NAME })
    
@login_required
def logout(request):
    auth_logout(request)
#     return render(request,"home.html" , {})
    return HttpResponseRedirect("/")

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")