function DeleteOrder() {
    let confirmation = prompt("You are about to delete the booking. \n Type 'yes' to confirm");
    if (confirmation.toLowerCase() == 'yes') {
        document.getElementById(elementId).remove();
        $.ajax({
            type: 'POST',
            url: '/cart/deletebooking/',
            data: {
                OrderId: orderID,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            
            success: ()=> alert('Booking deleted!')
        })
    }
}
