const red_header_element = document.getElementById("red_header");
//document.querySelector('#red_header')
const header_element = document.querySelector("header");

red_header_element.addEventListener('click', function() {
    header_element.style.color = "#FF0000"
})