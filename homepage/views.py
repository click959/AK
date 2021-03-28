from django.shortcuts import render , HttpResponse

sample_text = "Lorem ipsum dolor sit amet consectetur adipisicing elit.Consequuntur hic odio voluptatem tenetur consequatur.Lorem ipsum dolor sit amet consectetur adipisicing elit."
# Create your views here.
def index(request):     
    return render(request, 'index.html')


def home(request):
    comments = [{"body":sample_text , "name":"Jane Doe"} , 
                {"body":sample_text , "name":"Jane Doe"},
                {"body":sample_text , "name":"Jane Doe"} , 
                {"body":sample_text , "name":"Jane Doe"}]
    destinations = [{"name" : "Destination Name" , "body" :sample_text , "URL" : "/destination" , "imgurl" : "assets/img/destination.jpg"},
                    {"name" : "Destination Name" , "body" :sample_text , "URL" : "/destination", "imgurl" : "assets/img/destination.jpg"},
                    {"name" : "Destination Name" , "body" :sample_text , "URL" : "/destination", "imgurl" : "assets/img/destination.jpg"},
                    {"name" : "Destination Name" , "body" :sample_text , "URL" : "/destination", "imgurl" : "assets/img/destination.jpg"},
                    {"name" : "Destination Name" , "body" :sample_text , "URL" : "/destination", "imgurl" : "assets/img/destination.jpg"}]

    context = {"commentlist" : comments , 
               "destinations" : destinations}

    return render(request, 'home.html',context)


def about(request):
    return render(request , 'aboutus.html')


def contact(request):
    return render(request, 'contactus.html')

def error_404(request,exception):
    return render(request,'404.html')

def error(request):
    return render(request , 'error.html')

def error_400_403(request,exception):
    return render(request , 'error.html')