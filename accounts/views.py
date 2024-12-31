# ******view.py in python major function as get data, template display(html) and use for loop wait users request
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
# from django that mean library, import is shortcut or label name



#  Find register.html label id for user auth register function, 1 - 6 line is match register.html label
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name'] 
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        # if statement mean password not match, then pass user to register again to re input
        # in.py if statement function attenion to Intend line
        if password == password_confirm:
            if User.objects.filter(username = username).exists():
                messages.error(request, 'Username already taken')
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.error(request, 'Email already taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username = username, password = password, email = email, first_name = first_name, last_name = last_name)
                    user.save()
                    messages.success(request, 'You are now registered and can login')
                    return redirect('login')
        else:
            messages.error('password do not match')
        return redirect('register')
    else:
        return render(request,'accounts/register.html')

# Put 2 field to auth function validate
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You have logged in')
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect("login")
    else:
        return render(request,'accounts/login.html')
    

# Register / Login action use method POST,
# If success login, then give unique csrf token with time range for ex.1 hour, 
# CRUD main function , bz CUD is database in/out major right, expect Read function


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out!')
    return redirect('index')


def dashboard(request):
    user_contacts = Contact.objects.order_by("-contact_date").filter(user_id=request.user.id)
    context = {
        'contacts':user_contacts
    }
    return render(request,'accounts/dashboard.html',context)