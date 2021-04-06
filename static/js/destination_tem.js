// addToCart
console.log('ajax - django - ADD TO CART');

let id, priceId;
function AddToCart() {
    id = cid;
    priceId = priceid;
}
$(document).on('submit', id, function(e){
    e.preventDefault();

    numPeople = e.target[1].id;
    numRoom = e.target[2].id;
    fromDate = e.target[3].id;
    toDate = e.target[4].id;
    hotelId = e.target[5].id;
    roomId = e.target[6].id;

    numOfPeople = document.getElementById(numPeople).value;
    numOfRoom = document.getElementById(numRoom).value;
    fDate = document.getElementById(fromDate).value;
    tDate = document.getElementById(toDate).value;

    if (numOfPeople < numOfRoom && fDate < tDate) {
        alert('Number of rooms sohuld be less than or equal to number of peoples');
    } else if ((numOfPeople >= numOfRoom && fDate > tDate)){
        alert('to date should be after the from date');
    } else if ((numOfPeople < numOfRoom && fDate > tDate)) {
        alert('upar ke dono chutiye hain');
    } else {
        $.ajax({
            type: 'POST',
            url: '/cart/addtocart/',
            data: {
                numberOfPeople: numOfPeople,
                numberOfRoom: numOfRoom,
                fromDate: fDate,
                toDate: tDate,
                hotelId: document.getElementById(hotelId).value,
                roomId: document.getElementById(roomId).value,
                cost: document.getElementById(priceId).innerText,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function () {
                alert("Item added to cart");
                
                document.getElementById(numPeople).value = '';
                document.getElementById(numRoom).value = '';
                document.getElementById(fromDate).value = '';
                document.getElementById(toDate).value = '';
            }
        })
    }
});