from django.shortcuts import render , HttpResponse

# Create your views here.
def signup(request):
    return render(request , 'signup.html')

def login(request):
    return render(request , 'signin.html')

def userlogin(request):
    return HttpResponse("Okay")
