function searchCards() {
    // Get the input value from the search bar
    var input = document.getElementById("searchInput").value.toLowerCase();

    // Get all the cards on the page
    var cards = document.getElementsByClassName("card");

    // Loop through the cards and hide those that don't match the search term
    for (var i = 0; i < cards.length; i++) {
        var title = cards[i].querySelector(".card-title").textContent.toLowerCase();
        if (title.indexOf(input) > -1) {
            cards[i].style.display = "";
        } else {
            cards[i].style.display = "none";
        }
    }
}



