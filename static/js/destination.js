var cards = document.getElementsByClassName("card");
for(var i=0; i < cards.length ; i++) 
{
    var id = cards[i].id
    cards[i].addEventListener("click", function() {window.location.href = ("/destination/"+id)});
}
