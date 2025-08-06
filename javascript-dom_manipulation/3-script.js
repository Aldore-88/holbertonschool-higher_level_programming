const toggle_header_element = document.getElementById("toggle_header");
const header_element = document.querySelector("header");

toggle_header_element.addEventListener('click', function() {
        header_element.classList.toggle("red");
        header_element.classList.toggle("green");
})