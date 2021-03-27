from django.shortcuts import render , HttpResponse


# Create your views here.
def signupUser(request):
    return render(request , 'signup.html')

def loginUser(request):
    return render(request , 'signin.html')

def logoutUser(request):
    return HttpResponse("okay")
