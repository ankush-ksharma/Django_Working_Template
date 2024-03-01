from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/auth/login')
def signup(request):
    if not request.user.is_superuser:
        logout(request)
        messages.warning(request, 'You are not authorized to access this page. Login Again.')
        return redirect('/auth/login')
    if (request.method == "POST"):
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')

        if password != confirm_password:
            messages.warning(request, 'Password and Confirm Password are not same')
            return render(request, 'authentication/signup.html')
        
        try:
            if User.objects.filter(email=email):
                messages.warning(request, 'Email already exists')
                return render(request, 'authentication/signup.html')
            elif User.objects.filter(username=username):
                messages.warning(request, 'Username already exists')
                return render(request, 'authentication/signup.html')
            else:
                user = User.objects.create_user(email= email, username = username)
                user.set_password(password)
                user.save()
                messages.success(request, 'Registration Successful, Please Login to continue')
                return redirect('/auth/login')
        except Exception as e:
            pass

    return render(request, 'authentication/signup.html')


def handlelogin(request):
    if (request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.filter(username=username)
            if user.exists() and user.first().check_password(password):
                login(request, user.first())
                return redirect('/')
            else:
                messages.warning(request, 'Invalid username or password')
                return render(request, 'authentication/login.html')
        except Exception as e:
            pass
    return render(request, 'authentication/login.html')

@login_required(login_url='/auth/login/')
def handlelogout(request):
    logout(request)
    messages.info(request, "Logout Successfully")
    return redirect('/auth/login')

