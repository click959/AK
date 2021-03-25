from django.shortcuts import render , HttpResponse

des = {
        "id" : "20200325et122631",
        "imgURL" : "",
        "rating" : [1,1,1,1,0],
        "ratingnum" : "4.0",
        "name" : "The Dark Forest Adventure",
        "price" : 1870,
        "duration" : 3,
        "location" : "Agra"
    }
# Create your views here.
def destinations(request):
    destination = [des , des , des, des , des , des , des , des,des , des , des, des , des , des , des , des]
    context = {"destinationlist" : destination}
    return render(request , 'destination.html',context)

def destination(request , id = 0):
    #\d{8}\w[et]\d{6}
    return  HttpResponse("For page of id " + str(id))