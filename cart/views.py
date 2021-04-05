from django.shortcuts import render
from django.http import HttpResponse
from cart.models import order
from datetime import date, datetime

# Create your views here.
def AddToCart(request):
    if request.method == 'POST':
        hotelId = request.POST['hotelId']
        roomId = request.POST['roomId']
        numberOfPeople = request.POST['numberOfPeople']
        numberOfRoom = request.POST['numberOfRoom']
        fromDate = request.POST['fromDate']
        toDate = request.POST['toDate']
        cost = request.POST['cost']

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

        # calculating total cost
        totalCost = int(cost) * int(numberOfDays) * int(numberOfPeople)

        # getting user
        username = request.user

        # DatePaid : fromDate > from the bank
        # PaidStatus : False > True after successful payment
        # TransactionID : 'xxx' > from the bank
        
        myOrder = order(user=username, HotelId=hotelId,  roomId=roomId, orderId=orderId, NumberOfPeople=numberOfPeople, NumberOfRooms=numberOfRoom, FromDate=fromDate, ToDate=toDate, NumberOfDays=numberOfDays, Cost=totalCost, PaidStatus=False, TransactionID="xxx", DatePaid=fromDate)

        myOrder.save()

        return HttpResponse('')


def MyCart(request, id = 0):
    if request.user.is_authenticated:
        orderDetails = order.objects.all().filter(PaidStatus=False, user = request.user)
        if orderDetails.count() == 0:
            return HttpResponse('order do not exists')
        else:
            return render(request, 'cart.html', {"orderDetails": orderDetails})
    else:
        return render(request , 'signin.html')
