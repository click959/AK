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

    $.ajax({
        type: 'POST',
        url: '/cart/addtocart/',
        data: {
            numberOfPeople: document.getElementById(numPeople).value,
            numberOfRoom: document.getElementById(numRoom).value,
            fromDate: document.getElementById(fromDate).value,
            toDate: document.getElementById(toDate).value,
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
});