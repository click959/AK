var cards = document.getElementsByClassName("card");
for(var i=0; i < cards.length ; i++) 
{
    var id = cards[i].id
    cards[i].addEventListener("click", function() {url = "/destination/"+id;window.open(url, '_blank').focus()});
}
