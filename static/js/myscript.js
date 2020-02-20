$("document").ready(function() {
    // Get the modal
    var modal1 = document.getElementById("editModal");
    var modal2 = document.getElementById("deleteModal");
    // Get the button that opens the modal
    var btn1 = document.getElementById("editBtn");
    var btn2 = document.getElementById("deleteBtn");
    // Get the <span> element that closes the modal
    var span1 = document.getElementsByClassName("1")[0];
    var span2 = document.getElementsByClassName("2")[0];

    // When the user clicks on the button, open the modal
    btn1.onclick = function() { modal1.style.display = "block"; }
    btn2.onclick = function() { modal2.style.display = "block"; }
        // When the user clicks on <span> (x), close the modal
    span1.onclick = function() { modal1.style.display = "none"; }
    span2.onclick = function() { modal2.style.display = "none"; }
        // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal1) {
            modal1.style.display = "none";
        }
    }
    window.onclick = function(event) {
        if (event.target == modal2) {
            modal2.style.display = "none";
        }
    }
});