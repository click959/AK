from django.shortcuts import render , HttpResponse
from destinations import mongodbconn
from destinations import mongodb2conn

s = """All the cotent of the room and about the room 
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
                                tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                                quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo 
                                consequat. Duis aute irure dolor in reprehenderit in voluptate
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
                                tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                                quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo 
                                consequat. Duis aute irure dolor in reprehenderit in voluptate
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
                                tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                                quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo 
                                consequat. Duis aute irure dolor in reprehenderit in voluptate"""
full_des = {
    "id" : "20200325et122631",
    "img" : [{"url" : "img/landing.jpg" , "label" : "First slide label" , "comment" : "Nulla vitae elit libero, a pharetra augue mollis interdum."} , {"url" : "img/landing.jpg" , "label" : "Second slide label" , "comment" : "Praesent commodo cursus magna, vel scelerisque nisl consectetur."},{"url" : "img/landing.jpg" , "label" : "Third slide label" , "comment" : "Nulla vitae elit libero, a pharetra augue mollis interdum."},{"url" : "img/landing.jpg" , "label" : "Fourth slide label" , "comment" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit."}],
    "Name" : "Destination Name",
    "rating" : [1,1,1,1,0],
    "ratingnum" : "4.0",
    "about" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate",
    "duration" : 3,
    "location" : "Agra",
    "points" : ["Couple friendly" , "Beach Sports like Volleyball, Football, Badminton" , "Sea food available" , "Music System available" ],
    "Rooms" : [{"id": "type1" , "RoomType" : "Room for one" , "cost" : 500 , "imgURL" : "../static/img/landing.jpg" , "about" : s , "capacity" : 1 , "avail" : 10} , {"id": "type2" ,"RoomType" : "Room for two" , "cost" : 700 , "imgURL" : "../static/img/landing.jpg" , "about" : s, "capacity" : 2 , "avail" : 10} , {"id": "type3" ,"RoomType" : "Room for five" , "cost" : 600 , "imgURL" : "../static/img/landing.jpg" , "about" : s , "capacity" : 5, "avail" : 10}]
}
# Create your views here.
def destinations(request):
    destination = mongodbconn.fetch_All()
    context = {"destinationlist" : destination}
    return render(request , 'destination.html',context)

def destination(request , id = 0):
    #\d{8}\w[et]\d{6}
    full_des = mongodb2conn.fetch_one(id)
    if(full_des == None):
        return HttpResponse("No page such found")
    context = full_des
    response = render(request , 'destination_template.html' , context) 
    response.set_cookie(key="lastdestinationvisit" , value= full_des['id'] , httponly=True)
    return response