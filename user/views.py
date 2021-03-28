from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from user.models import Profile
import hashlib

# Create your views here.
def signupUser(request):

    if request.method == 'POST':
        fname = request.POST['fname']
        email = request.POST['email']
        pnumber = request.POST['pnumber']
        dob = request.POST['dob']
        password = request.POST['password']
        print(email)
        username = hashlib.sha512(email.encode()).hexdigest()
        try:
            User.objects.get(username=username)
            return render(request , 'signup.html' , {"alert" : 1})
        except:
            user = User.objects.create_user(username = username , email = email , password = password)
            user.first_name = fname
            obj = Profile(user = user , phone = pnumber , DOB = dob)
            obj.save()
            user.save()

            return render(request , 'signup.html' , {"alert" : 0})

    return render(request , 'signup.html')

def loginUser(request):
    
    urltoredirect = ""
    try:
        value = request.COOKIES.get('lastdestinationvisit')
        urltoredirect += value
    except:
        print("Error")

    if request.user.is_authenticated:
        return render(request , "signin.html" , {"alert" : 0 , "reurl" : urltoredirect})

    if request.method == 'POST':
        print(urltoredirect)
        email = request.POST['email']
        password = request.POST['password']
        email = email.lower()
        username = hashlib.sha512(email.encode()).hexdigest()
        user = authenticate(request, username= username, password=password)
        if user is not None:
            login(request,user)
            return render(request , "signin.html" , {"alert" : 0 , "reurl" : urltoredirect})
        else:
            return render(request , "signin.html" , {"alert" : 1})        
    return render(request , 'signin.html')

def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponse("okay")
    else:
        return render(request , 'signin.html') 
