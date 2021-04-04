from django.shortcuts import render
from django.http import HttpResponse
from cart.models import order
from datetime import date, datetime

# Create your views here.
def AddToCart(request):
    if request.method == 'POST':
        numberOfPeople = request.POST['numberOfPeople']
        numberOfRoom = request.POST['numberOfRoom']
        fromDate = request.POST['fromDate']
        toDate = request.POST['toDate']

        # calculating number of days
        fdate = fromDate.split('-')
        tdate = toDate.split('-')
        DateFrom = date(int(fdate[0]), int(fdate[1].lstrip("0")), int(fdate[2].lstrip("0")))
        DateTo = date(int(tdate[0]), int(tdate[1].lstrip("0")), int(tdate[2].lstrip("0")))
        numberOfDays = ((DateTo - DateFrom).days)

        # loading current date time for generating below id's
        curDateTime = datetime.now()

        # Order Id > FORMAT: od20210329t120731
        orderId = 'od' + curDateTime.strftime("%x").replace('/', '') + 't' + curDateTime.strftime("%X").replace(':', '')
        # Hotel Id > FORMAT: 20210329et120731
        hotelId = curDateTime.strftime("%x").replace('/', '') + 'et' + curDateTime.strftime("%X").replace(':', '')

        # getting user
        username = request.user

        # Cost : 700 > from db
        # DatePaid : fromDate > from the bank
        # roomId : 101 > ot be decided
        # PaidStatus : False > True after successful payment
        # TransactionID : 'xxx' > from the bank
        
        myOrder = order(user=username, HotelId=hotelId,  roomId="101", orderId=orderId, NumberOfPeople=numberOfPeople, NumberOfRooms=numberOfRoom, FromDate=fromDate, ToDate=toDate, NumberOfDays=numberOfDays, Cost=700, PaidStatus=False, TransactionID="xxx", DatePaid=fromDate)

        myOrder.save()

        return HttpResponse('')


def MyCart(request):
    return render(request, 'cart.html')